##pdf4
##want to make pdf file with 4 pages merged into 1
##auto loaded a directory walk, swap method to own purposes.

import PyPDF2, os

def pdf4(filename):
    if filename.endswith('.pdf'):
        pdfFileObj = open(filename, 'rb') #read binary mode
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj) #parse
        if not pdfReader.isEncrypted:
            pdfOutputFile = open(filename[:-4] + "4.pdf", 'wb')
            pdfWriter = PyPDF2.PdfFileWriter()
            numberofpages = pdfReader.numPages
            pg = 0
            while pg < numberofpages:
                
                a=pdfReader.getPage(pg)
                b=pdfReader.getPage(pg+1)
                #c=pdfReader.getPage(pg+2)
                #d=pdfReader.getPage(pg+3)
                    
                #pageObj = pdfReader.getPage(pg)
                #if (a.mediaBox.upperRight[0]+b.mediaBox.upperRight[0])>(c.mediaBox.upperRight[0]+d.mediaBox.upperRight[0]): w=(a.mediaBox.upperRight[0]+b.mediaBox.upperRight[0])
                #else: w=(c.mediaBox.upperRight[0]+d.mediaBox.upperRight[0])
                #if (a.mediaBox.upperRight[1]+c.mediaBox.upperRight[1])>(b.mediaBox.upperRight[1]+d.mediaBox.upperRight[1]): h=(a.mediaBox.upperRight[1]+c.mediaBox.upperRight[1])
                #else: h=(b.mediaBox.upperRight[1]+d.mediaBox.upperRight[1])
                
                w=int(a.mediaBox.upperRight[0]+b.mediaBox.upperRight[0])
                h=int(a.mediaBox.upperRight[1])
                four=PyPDF2.pdf.PageObject.createBlankPage(width=w, height=h)
                print(w,h)
                #want to merge whatever into the above blank.
                
                four.mergeTranslatedPage(a, tx=0, ty=0)
                #four.mergeTranslatedPage(b, tx=int(a.mediaBox.upperRight[1]), ty=0)
                #four.mergePage(a)
                
                pdfWriter.addPage(four)
                pg = pg + 4
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
                pdf4(filename)
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
    
