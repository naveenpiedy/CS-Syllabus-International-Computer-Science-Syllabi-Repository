#-*- coding: utf-8 -*-
from pdfminer import pdfinterp
from pdfminer.pdfparser import PDFDocument,PDFPage,PDFParser
from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator


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

    url='C:\\Users\\hasee\\Desktop\\Syllabus_SER518-Spring2018.pdf'
    # url = 'C:\\Users\\hasee\\Desktop\\syllabus.pdf'
    output=doPDF(url)
    print(output)
    lowered_output=output.lower()
    index01=lowered_output.find('instru')
    index02=lowered_output.find('descr')
    index03=lowered_output.find('summary')
    if index01!= -1:
        print(output[index01:index01+120])
    if index02!= -1:
        print(output[index02:index02+300])
    elif index03!= -1:
        print(output[index03:index03+300])
    else:
        pass
