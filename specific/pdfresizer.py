##pdfresize
##outputs a resized (scaled) copy of a pdf file in same directory as originals
##auto loaded a directory walk, swap method to own purposes.
##Shit, doesnt reduce pdf file size though....

import PyPDF2, os

def pdfresize(filename):
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
            pdfWriter.write(pdfOutputFile)
        pdfFileObj.close()
        pdfOutputFile.close()




print('In which directory do you want to search? Provide input of the form: C:\dir1\subdir1\subdir2')
userdir = str(input())
dirfiles = os.listdir(userdir)

##os.walk method; loops for all files and subdirectories
for dirpath, subdirs, files in os.walk(userdir):
    for filename in files:
        if os.path.isfile(str(dirpath) + "\\" + filename):
            filename = os.path.join(os.path.abspath(dirpath), filename)
            try:
                pdfresize(filename)
            except: continue


##Folder only option; loops only for all files, no subdirectories
#for i in range(len(dirfiles)):
#    filename = dirfiles[i]
#    readdpath = re.compile(r'[a-zA-Z]\:\\') #re of something like "C:\\"
#    if not readdpath.search(filename): filename = os.path.join(os.getcwd(), filename) #fills in full path into filename if user lazy
#    try: fileread(filename)
#    except: continue

##Specific file option; no file looping
#print('Which file do you want to read? Provide input of the form: C:\\dir1\\subdir1\\file1')
#filename = str(input())
#readdpath = re.compile(r'[a-zA-Z]\:\\') #re of something like "C:\\"
#if not readdpath.search(filename): filename = os.path.join(os.getcwd(), filename)
#fileread(filename)
    
