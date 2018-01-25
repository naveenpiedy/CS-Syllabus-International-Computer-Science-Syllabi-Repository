import PyPDF2

pdfFile = open('demo1.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFile)
numPages = pdfReader.numPages

print numPages

pageObj = pdfReader.getPage(0)

print pageObj.extractText()