#-*- coding: utf-8 -*-
from pdfminer import pdfinterp
from pdfminer.pdfparser import PDFDocument,PDFPage,PDFParser
from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator
import re

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

if __name__=='__main__':

    # url='C:\\Users\\hasee\\Desktop\\Syllabus_SER518-Spring2018.pdf'
    url = 'C:\\Users\\hasee\\Desktop\\SER516-Syllabus-Spring2017.pdf'
    output=doPDF(url)
    # print(output)
    lowered_output=output.lower()
    index01=lowered_output.find('topic')
    index02=lowered_output.find('descr')
    index03=lowered_output.find('summa')
    if index01!=-1:
        str01=output[index01:]
        spl01=re.split(r'\n\n',str01)
        print(spl01[0])
    else:
        pass


    if index02!= -1:
        str02=output[index02:]
        spl02=re.split(r'\n\n',str02)
        print(spl02[0])

    elif index03!= -1:
        str03=output[index03]
        spl03=re.split(r'\n\n',str03)
        print(spl03[0])
    else:
        pass
