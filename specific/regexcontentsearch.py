# Opens all .txt files in a folder only, or including subfolders and
# then searches for any line that matches
# a user-supplied regular expression.
# saves path, filename, location, line into .txt file

import os
import re

print('In which directory do you want to search? Provide input of the form: C:\dir1\subdir1\subdir2')
userdir = str(input())
dirfiles = os.listdir(userdir)

#creates dumpfile, commits to secondary memory, reopens in append mode.
dumpfile = open('C:\\Users\\a0094\\Desktop\\dump.txt', 'w')
dumpfile.close
dumpfile = open('C:\\Users\\a0094\\Desktop\\dump.txt', 'a')


print('What text do you want to search for? Provide Regex, or string simply')
userReg = str(input())
stringRegex = re.compile(userReg)
fileRegex = re.compile(r'\w+\.txt')

#Directory walk option
for dirpath, subdirs, files in os.walk(userdir):
    for file in files:
        try: 
            openfile = open(file)
            readFile = openfile.readlines()
        except: continue
        linenumber = int(0)
        for r in readFile:
            if stringRegex.search(r): 
                print(dirpath + "\\" + file, "line " + str(linenumber), r)
                dumpfile.write(dirpath + "\\" + file + " line " + str(linenumber) + " " + r)
            linenumber = linenumber + 1
            
#Folder only option
#for i in range(len(dirfiles)):
#    if fileRegex.search(dirfiles[i]):
#        openFile = open(userdir + "\\" + dirfiles[i])
#        readFile = openFile.readlines()
#        linenumber = int(0)
#        for r in readFile:
#            if stringRegex.search(r):
#                print(userdir + "\\" + dirfiles[i], "line " + str(linenumber), r)
#                dumpfile.write(userdir + "\\" + dirfiles[i] + " line " + str(linenumber) + " " + r)
#            linenumber = linenumber + 1

dumpfile.close




