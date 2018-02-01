import os

from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from django.core.files.storage import FileSystemStorage
# from signupapp.models import UserTable
from pdfminer import pdfinterp
from pdfminer.pdfparser import PDFDocument,PDFPage,PDFParser
from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator
import re

# def index(request):
#     return render(request, 'homeapp/dashboard.html')

def index(request):
    c = {}
    c.update(csrf(request))
    First_Name = ""
    Last_Name = ""
    Email = ""
    Username = ""
    University = ""
    IsPro = ""
    # usertable = UserTable()
    if request.method == 'POST':
        myfile=request.FILES['file_path']
        fs = FileSystemStorage()
        saved_file=fs.save(myfile.name,myfile)
        fs.url(saved_file)
        str = os.path.join(settings.MEDIA_ROOT, myfile.name)
        result=doPDF(str)
        final_result=extractInfo(result)
        print(final_result)

    if request.user.is_authenticated:
        First_Name = request.user.first_name
        Last_Name = request.user.last_name
        Email = request.user.email
        Username = request.user.username
        University = request.user.userinfo.university
        IsPro = request.user.userinfo.isprofessor
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