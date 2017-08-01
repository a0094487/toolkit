
if filename.endswith('.pdf'):
    pdfFileObj = open(filename, 'rb') #read binary mode
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) #parse
    if not pdfReader.isEncrypted:
        pdfOutputFile = open(filename[:-4] + "scaled.pdf", 'wb')
        pdfWriter = PyPDF2.PdfFileWriter()
        numberofpages = pdfReader.numPages
        pg = 0 
        while pg < numberofpages:
            pageObj = pdfReader.getPage(pg)
            (w, h) = pageObj.mediaBox.upperRight
            #.getUpperRight_x(), .getUpperRight_y()
            height=1000  # i want height=1000. Scaled.
            width= w * height / h
            pageObj.scaleTo(width, height)
            pdfWriter.addPage(pageObj)
            pg = pg + 1
            dataobject[filename][pg]=pageObj.extractText()
    pdfFileObj.close()
    pdfWriter.write(pdfOutputFile)
    pdfOutputFile.close()
