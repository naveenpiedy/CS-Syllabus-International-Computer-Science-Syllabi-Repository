import os

from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from django.core.files.storage import FileSystemStorage
from signupapp.models import UserTable
from pdfminer import pdfinterp
from pdfminer.pdfparser import PDFDocument,PDFPage,PDFParser
from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator
from .models import PDF
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
    total_tag=[]
    pdf_obj = PDF()

    if request.user.is_authenticated:
        First_Name = request.user.first_name
        Last_Name = request.user.last_name
        Email = request.user.email
        Username = request.user.username
        pdf_obj.uploaders = Username
        University = request.user.userinfo.university
        IsPro = request.user.userinfo.isprofessor

    if request.method == 'POST':
        myfile = request.FILES['file_path']
        if not myfile.name.isspace() and myfile.name != '':
            fs = FileSystemStorage()
            saved_file = fs.save(myfile.name, myfile)
            fs.url(saved_file)
            str = os.path.join(settings.MEDIA_ROOT, myfile.name)
            result = doPDF(str)
            final_result = extractInfo(result)
            pdf_obj.pdf_desc = final_result

            prof_name = request.POST['professor']
            univ_name = request.POST['university']
            subj_name = request.POST['subjectname']

            tag1 = request.POST['tag1']
            k1 = tag1.strip()
            if k1 != '':
                total_tag.append(k1)

            tag2 = request.POST['tag2']
            k2 = tag2.strip()
            if k2 != '':
                total_tag.append(k2)

            tag3 = request.POST['tag3']
            k3 = tag3.strip()
            if k3 != '':
                total_tag.append(k3)
            print('Prof_name: ' + prof_name)
            print('Univ_name: ' + univ_name)
            print('Subj_name: ' + subj_name)
            print(total_tag)
            pdf_obj.pdf_tags = total_tag
            pdf_obj.pdfName = myfile.name
            pdf_obj.professor_name = prof_name
            pdf_obj.subjectName = subj_name
            pdf_obj.university = univ_name
            pdf_obj.save()

    return render(request, 'homeapp/dashboard.html', {
        'First_Name': First_Name, 'Last_Name' : Last_Name, 'Email_Address' : Email, 'Username' : Username,
        'University' : University, 'Isprofessor' : IsPro
    })

def doPDF(url):
    fp = open(url, 'rb')
    parser=PDFParser(fp)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)
    doc.initialize()

    resource_manager=pdfinterp.PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(resource_manager, laparams=laparams)
    interpreter = pdfinterp.PDFPageInterpreter(resource_manager, device)
    pages=doc.get_pages()
    str=''
    for page in pages:
        interpreter.process_page(page)
        layout=device.get_result()
        for x in layout:
            if isinstance(x,LTText):
                str+=x.get_text()
    return str

def extractInfo(str):
    final_result=''
    lowered_output = str.lower()
    index01 = lowered_output.find('topic')
    index02 = lowered_output.find('descr')
    index03 = lowered_output.find('summa')
    if index01 != -1:
        str01 = str[index01:]
        spl01 = re.split(r'\n\n', str01)
        final_result+=spl01[0]

    if index02 != -1:
        str02 = str[index02:]
        spl02 = re.split(r'\n\n', str02)
        final_result += spl02[0]
        return final_result

    elif index03 != -1:
        str03 = str[index03:]
        spl03 = re.split(r'\n\n', str03)
        final_result+=spl03[0]
        return final_result
    else:
        return ''

def edit_profile(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated:
        checked = ""
        First_Name = request.user.first_name
        Last_Name = request.user.last_name
        #Email = request.user.email
        #Username = request.user.username
        University = request.user.userinfo.university
        IsPro = request.user.userinfo.isprofessor
        if IsPro:
            checked = 'checked'
    if request.method == 'POST' and request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        ut = UserTable.objects.get(user=user)
        print(request.POST)
        if not request.POST['first_name'].isspace() and request.POST['first_name']!='':
            user.first_name = request.POST['first_name']
        if not request.POST['last_name'].isspace() and request.POST['last_name']!='':
            user.last_name = request.POST['last_name']
        if not request.POST['university'].isspace() and request.POST['university']!='':
            ut.university = request.POST['university']

        if 'isProfessor' in request.POST:
            IsPro=True
        else:
            IsPro=False
        ut.isprofessor=IsPro
        uuser = authenticate(username=user.username, password=request.POST['old_password'])
        if uuser is not None:
            if not request.POST['new_password'].isspace() and request.POST['new_password']!='':
                if request.POST['new_password'] == request.POST['retype_new_password']:
                    print("Yeahhh")
                    user.set_password(request.POST['new_password'])
                    #updr.save()ate_session_auth_hash(request, user)

        user.save()
        ut.save()



    return render(request, 'homeapp/editprofile.html',{
        'First_Name': First_Name, 'Last_Name' : Last_Name,
        'University' : University, 'checked': checked,
    }, c)

def see_uploaded(request):
    c = {}
    c.update(csrf(request))
    print(request.POST)
    if request.method=='POST':
        if request.POST['Delete']:
            delete_id=request.POST['Delete']
            spe_pdf=PDF.objects.get(id=delete_id)
            spe_pdf.delete()

    if request.user.is_authenticated:
        user_name=request.user.username
        pdfs = PDF.objects.filter(uploaders=user_name)
        list=[]
        for one_pdf in pdfs:
            list.append([one_pdf.id,one_pdf.pdfName])


    return render(request,'homeapp/uploaded.html',{'List':list},c)

def edit_content(request):
    c = {}
    c.update(csrf(request))
    print(request.POST)
    edit_list=[]
    if request.method=='POST':
        if request.POST['Edit']:
            edit_str=request.POST['Edit']
            edit_id=request.POST['id']
            edit_pdf=PDF.objects.get(id=edit_id)
            edit_pdf.pdf_desc=edit_str
            edit_pdf.save()
            edit_list.append(edit_id)
            edit_list.append(edit_str)
    return render(request,'homeapp/edit_content.html',{'List':edit_list},c)
