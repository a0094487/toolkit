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
dumpfile = open(userdir+'\\dump.txt', 'w')
dumpfile.close
dumpfile = open(userdir+'\\dump.txt', 'a')

print('What text do you want to search for? Provide Regex, or string simply')
userReg = str(input())
stringRegex = re.compile(userReg)

#sample complex re object plus sample extraction.
#datePattern = re.compile(r'''^(.*?) #All text before date: (1)
#                         ((0|1)?\d)- #One or two month digits:(3) within (2) 
#                         ((0|1|2|3)?\d)- #One or two digits for date: (5) within (4)
#                         ((19|20)\d\d) #Four digits for the year: (7) within (6)
#                         (.*?)$ #all text after the date: (8)
#                         ''', re.VERBOSE)
#datePattern.search(somestring1).group(4) #returns string satisfying group 4 

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
#fileRegex = re.compile(r'\w+\.txt')
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
