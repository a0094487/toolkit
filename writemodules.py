##Writing modules, csv writing, directory organization, and excel writing
import csv, os, shutil, openpyxl

## Write out a CSV file.
## Just flat rows for now, .writerow only good for list of values, 
## will need to prepare dataobject into flatdataobject; lists of value before write. 
csvFileObj = open('desiredfilename.csv', 'w', newline='') #newline for "technical reasons".
csvWriter = csv.writer(csvFileObj)
#csvWriter = csv.writer(csvFileObj, delimeter='\t') #for .tsv file
for list in flatdataobject:
    csvWriter.writerow(list)
csvFileObj.close()


## Organzing and ferrying files and folders around
destinationfolder = "C:\\subfolders\\newdestinationfoldername"
if not os.path.exists(destinationfolder): os.makedirs(destinationfolder) #addresses invalid paste because without valid directory
shutil.move(orginalfilename, os.path.join(destinationfolder, newfilename)) # cuts file with 1st filename and pastes a copy with 2nd filename.  
#shutil.copy(originalFilename, destinationfolder) # makes copies into folder
#shutil.move(originalFilename, destinationfolder) # cut-paste into folder


## Writes into excel, optional various worksheets component
wb = openpyxl.Workbook()    
try: 
    wb.remove_sheet_by_name('Sheet2') #operation for cleaning default opensheets for some xlsx versions
    wb.remove_sheet_by_name('Sheet3')
except: pass
## addons for multiple worksheets
#sheet = wb.get_sheet_by_name('somesheetname')
#sheet.title = 'someothersheetname' #consider linking up to a high level key in dictionary, loop, for a workbook with many worksheets
#sheet = wb.get_sheet_by_name('someothersheetname')
#wb.create_sheet(index=0, title='somesheetname') #indexed as 0th sheet
worksheets = workbook.get_sheet_names()
numofworksheets = count(worksheets)
lastworksheetname = worksheets[numofworksheets-1]
sheet = wb.get_sheet_by_name(lastworksheetname)
## dataobject dictionary format addon loop
#for keyvaluepairs in dataobject:
#    sheettitle=str(keyvaluepairs[0]) #sheet title = key
#    wb.create_sheet(title=sheettitle)
#    #wb.create_sheet(index=0, title='somesheetname') #indexed as 0th sheet
#    sheet = wb.get_sheet_by_name(sheettitle)
#    flatdataobject = keyvaluepairs[1] # interface with below single sheet write loop
##single sheet write loop
i=1
for list in flatdataobject: #assuming here flatdataobject as dict/list of lists of values, mod as you see fit.
    j=1
    for valueiwant in list:
        sheet.cell(row=i, column=j).value = valueiwant
        j = j + 1
    i = i + 1
wb.save(newfilename)