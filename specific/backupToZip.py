# backupToZip.py
# Copies an entire folder and its contents into
# a zip file whose filename embeds datetime, or increments.

import zipfile, os

def backupToZip(folder):
    # Backup the entire contents of "folder" into a zip file.

    folder = os.path.abspath(folder) # make sure folder is absolute

    # Figure out for the zip file this code should used based on 
    # how many zip files already exist, and renames new copy accordingly.
    #number = 1
    #while True:
    #    zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
    #    if not os.path.exists(zipFilename):
    #        break
    #    number = number + 1
    
    #alternatively: names copy by datetime
    zipFilename = os.pth.basename(folder) + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.zip'
    
    # Create the zip file.
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
                continue # don't backup the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')

print('Which directory do you want to backup? Provide input of the form: C:\dir1\subdir1\subdir2')
fn = str(input()) 
backupToZip(fn)

#I want to implement with datatimenow()