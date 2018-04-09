import os

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from django.core.files.storage import FileSystemStorage
from signupapp.models import UserTable
from pdfminer import pdfinterp
from pdfminer.pdfparser import PDFDocument, PDFPage, PDFParser
from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator
from .models import PDF
from .models import Tag
import re


# def index(request):
#     return render(request, 'homeapp/dashboard.html')

def index(request):
    c = {}
    c.update(csrf(request))
    print(request.POST)
    First_Name = ""
    Last_Name = ""
    Email = ""
    Username = ""
    University = ""
    IsPro = ""
    total_tag = []
    pdf_obj = PDF()
    tag_obj1 = Tag()
    tag_obj2 = Tag()
    tag_obj3 = Tag()

    if request.user.is_authenticated:
        First_Name = request.user.first_name
        Last_Name = request.user.last_name
        Email = request.user.email
        Username = request.user.username
        pdf_obj.uploaders = Username
        University = request.user.userinfo.university
        IsPro = request.user.userinfo.isprofessor
    else:
        return redirect("/login")

    if request.method == 'POST':
        myfile = request.FILES['file_path']
        if not myfile.name.isspace() and myfile.name != '':
            fs = FileSystemStorage()
            saved_file = fs.save(myfile.name, myfile)
            fs.url(saved_file)
            str = os.path.join(settings.MEDIA_ROOT, myfile.name)
            result = doPDF(str)
            final_result = extractInfo(result)
            if len(final_result) > 0:
                pdf_obj.pdf_topic = final_result[0]
            if len(final_result) > 1:
                pdf_obj.pdf_desc = final_result[1]

            prof_name = request.POST['professor']
            univ_name = request.POST['university']
            subj_name = request.POST['subjectname']
            pdf_year = request.POST['dropdown']
            tag1 = request.POST['tag1']
            k1 = tag1.strip()
            if k1 != '':
                total_tag.append(k1.lower())
                if not Tag.objects.filter(tagName=k1.lower()).exists():
                    tag_obj1.tagName = k1.lower()
                    tag_obj1.save()

            tag2 = request.POST['tag2']
            k2 = tag2.strip()
            if k2 != '':
                total_tag.append(k2.lower())
                if not Tag.objects.filter(tagName=k2.lower()).exists():
                    tag_obj2.tagName = k2.lower()
                    tag_obj2.save()

            tag3 = request.POST['tag3']
            k3 = tag3.strip()
            if k3 != '':
                total_tag.append(k3.lower())
                if not Tag.objects.filter(tagName=k3.lower()).exists():
                    tag_obj3.tagName = k3.lower()
                    tag_obj3.save()

            print('Prof_name: ' + prof_name)
            print('Univ_name: ' + univ_name)
            print('Subj_name: ' + subj_name)
            print(total_tag)
            pdf_obj.pdf_tags = total_tag
            pdf_obj.pdfName = myfile.name
            pdf_obj.professor_name = prof_name
            pdf_obj.subjectName = subj_name
            pdf_obj.university = univ_name
            pdf_obj.year = pdf_year
            pdf_obj.save()
            tag_group = pdf_obj.pdf_tags
            for each_tag in tag_group:
                record = Tag.objects.get(tagName=each_tag)
                print('+_+_+_')
                print(record)
                print(pdf_obj.year)
                if pdf_obj.year == 'Freshman':
                    record.freshman = True
                if pdf_obj.year == 'Junior':
                    record.junior = True
                if pdf_obj.year == 'Masters':
                    record.master = True
                if pdf_obj.year == 'Doctorate':
                    record.phD = True
                if pdf_obj.year == 'Senior':
                    record.senior = True
                if pdf_obj.year == 'Sophomore':
                    record.sophomore = True
                record.save()
            id_list = []
            user_uploaded = PDF.objects.filter(uploaders=Username)
            for upl in user_uploaded:
                id_list.append(upl.id)
            max_id = max(id_list)
            print(max_id)
            return redirect('edit_content', id=max_id)

    return render(request, 'homeapp/dashboard.html', {
        'First_Name': First_Name, 'Last_Name': Last_Name, 'Email_Address': Email, 'Username': Username,
        'University': University, 'Isprofessor': IsPro
    })


def doPDF(url):
    fp = open(url, 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)
    doc.initialize()

    resource_manager = pdfinterp.PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(resource_manager, laparams=laparams)
    interpreter = pdfinterp.PDFPageInterpreter(resource_manager, device)
    pages = doc.get_pages()
    str = ''
    for page in pages:
        interpreter.process_page(page)
        layout = device.get_result()
        for x in layout:
            if isinstance(x, LTText):
                str += x.get_text()
    return str


def extractInfo(str):
    final_result = []
    topic_str = ''
    des_sum = ''
    lowered_output = str.lower()
    index01 = lowered_output.find('topic')
    index02 = lowered_output.find('descr')
    index03 = lowered_output.find('summa')
    if index01 != -1:
        str01 = str[index01:]
        spl01 = re.split(r'\n\n', str01)
        topic_str += spl01[0]
        final_result.append(topic_str)

    if index02 != -1:
        str02 = str[index02:]
        spl02 = re.split(r'\n\n', str02)
        des_sum += spl02[0]
        final_result.append(des_sum)
        return final_result

    elif index03 != -1:
        str03 = str[index03:]
        spl03 = re.split(r'\n\n', str03)
        des_sum += spl03[0]
        final_result.append(des_sum)
        return final_result
    else:
        return final_result


def edit_profile(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated:
        checked = ""
        First_Name = request.user.first_name
        Last_Name = request.user.last_name
        # Email = request.user.email
        # Username = request.user.username
        University = request.user.userinfo.university
        IsPro = request.user.userinfo.isprofessor
        if IsPro:
            checked = 'checked'

    if request.method == 'POST' and request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        ut = UserTable.objects.get(user=user)
        print(request.POST)
        if not request.POST['first_name'].isspace() and request.POST['first_name'] != '':
            user.first_name = request.POST['first_name']
        if not request.POST['last_name'].isspace() and request.POST['last_name'] != '':
            user.last_name = request.POST['last_name']
        if not request.POST['university'].isspace() and request.POST['university'] != '':
            ut.university = request.POST['university']

        if 'isProfessor' in request.POST:
            IsPro = True
        else:
            IsPro = False
        ut.isprofessor = IsPro
        uuser = authenticate(username=user.username, password=request.POST['old_password'])
        if uuser is not None:
            if not request.POST['new_password'].isspace() and request.POST['new_password'] != '':
                if request.POST['new_password'] == request.POST['retype_new_password']:
                    print("Yeahhh")
                    user.set_password(request.POST['new_password'])
                    # updr.save()ate_session_auth_hash(request, user)

        user.save()
        ut.save()

        return redirect('/homeapp')

    else:
        return render(request, 'homeapp/editprofile.html', {
            'First_Name': First_Name, 'Last_Name': Last_Name,
            'University': University, 'checked': checked,
        }, c)


def see_uploaded(request):
    c = {}
    c.update(csrf(request))
    print(request.POST)
    if request.method == 'POST':
        if 'Delete' in request.POST:
            delete_id = request.POST['Delete']
            spe_pdf = PDF.objects.get(id=delete_id)
            spe_pdf.delete()
        elif 'Edit' in request.POST:
            edit_id = request.POST['Edit']
            return redirect('edit_content', id=edit_id)

    if request.user.is_authenticated:
        user_name = request.user.username
        pdfs = PDF.objects.filter(uploaders=user_name)
        list = []
        for one_pdf in pdfs:
            list.append([one_pdf.id, one_pdf.pdfName])
    print(list)
    return render(request, 'homeapp/uploaded.html', {'List': list}, c)


def edit_content(request, id):
    c = {}
    print(id)
    c.update(csrf(request))
    print(request.POST)
    if request.user.is_authenticated:
        user_name = request.user.username
        # pdfs = PDF.objects.filter(uploaders=user_name)
        # list = []
        # for one_pdf in pdfs:
        #     list.append(one_pdf.id)
        # max_id = max(list)
        spec_pdf = PDF.objects.get(uploaders=user_name, id=id)
        if request.method == 'POST' and request.POST['upload']:
            print("_+_+_+_+_+_+_+_+_+_+")
            new_desc = request.POST['Description']
            new_topic = request.POST['Topics']
            new_prof = request.POST['professor']
            new_univ = request.POST['university']
            new_sub = request.POST['subjectname']
            new_tag1 = request.POST['tag1']
            new_tag2 = request.POST['tag2']
            new_tag3 = request.POST['tag3']
            new_list = [new_tag1, new_tag2, new_tag3]

            spec_pdf.pdf_desc = new_desc
            spec_pdf.professor_name = new_prof
            spec_pdf.university = new_univ
            spec_pdf.subjectName = new_sub
            spec_pdf.pdf_tags = new_list
            spec_pdf.pdf_topic = new_topic
            spec_pdf.save()
            return render(request, 'homeapp/EditSyllabus.html', {
                'Description': new_desc, 'professor': new_prof, 'university': new_univ, 'subjectname': new_sub,
                'Topics': new_topic,
                'tag1': new_tag1, 'tag2': new_tag2, 'tag3': new_tag3
            })
        else:
            tag1 = ''
            tag2 = ''
            tag3 = ''
            if len(spec_pdf.pdf_tags) > 0:
                tag1 = spec_pdf.pdf_tags[0]
            if len(spec_pdf.pdf_tags) > 1:
                tag2 = spec_pdf.pdf_tags[1]
            if len(spec_pdf.pdf_tags) > 2:
                tag3 = spec_pdf.pdf_tags[2]

            return render(request, 'homeapp/EditSyllabus.html', {
                'Description': spec_pdf.pdf_desc, 'professor': spec_pdf.professor_name,
                'university': spec_pdf.university, 'Topics': spec_pdf.pdf_topic,
                'subjectname': spec_pdf.subjectName, 'tag1': tag1, 'tag2': tag2, 'tag3': tag3
            })

    return render(request, 'homeapp/EditSyllabus.html', c)
