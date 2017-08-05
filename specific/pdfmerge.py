# Chapter 13 Project Combining Select Pages from Many PDF's
# Combines all PDF's in the specified directory into a single PDF

import PyPDF2
import os

print('In which directory do you want to merge pdf files? Provide input of the form: C:\\dir1\\subdir1\\subdir2')
fn = str(input()) 

pdfFiles = []
for filename in os.listdir(fn):
    if filename.endswith('.pdf'):
        pdfFiles.append(os.path.join(fn, filename))
pdfFiles.sort(key = str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    #for pageNum in range(5, 7): #sample modification; if say, you only want to copy every 5th, 6th, 7th page.
    for pageNum in range(0, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

pdfOutput = open(os.path.join(fn, 'Combined.pdf'), 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
