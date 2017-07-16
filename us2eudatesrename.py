#filename pattern search organizing multitool

import os
import re
import shutil
#covering all multiple conditions to be met, in structured format.
datePattern = re.compile(r'''^(.*?) #All text before date: (1)
                         ((0|1)?\d)- #One or two month digits:(3) within (2) 
                         ((0|1|2|3)?\d)- #One or two digits for date: (5) within (4)
                         ((19|20)\d\d) #Four digits for the year: (7) within (6)
                         (.*?)$ #all text after the date: (8)
                         ''', re.VERBOSE)
#loops over each file with american dates in default directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
#scans filename, returns list of strings satisfying each datePattern conditions
    #if amerFilename.endswith('.txt'): continue #this selects against .txts
    if mo == None:
        continue

    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename) # cuts file with 1st filename and pastes a copy with 2nd filename.  
    #newfolder = "C:\\pdffolder"
    #if not os.path.exists(newfolder): os.makedirs(newfolder) #addresses invalid paste because without valid directory
    #shutil.copy(euroFilename, newfolder) # makes copies into folder
    #shutil.move(euroFilename, newfolder) # cut-paste into folder
    #print('Copying ' + euroFilename + '...')
#see regextxtsearchdump for reference to implement os.walk method
