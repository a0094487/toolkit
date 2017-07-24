##resizes files in a directory filewalk to 500*x, keeping aspect ratio.
##option 1: saves into seperate folder '\\resized'
##option 2: saves into same subdirectory for each file.
##requires pillow.

from PIL import Image
import os

def resizepic(filename):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        
        picture = Image.open(absfilename)
        width, height = picture.size
        print(picture.size)
        modheight = int(int(height) * 500 / int(width))
        print(modheight)
        resized = picture.resize((500,modheight))
        #resized.save(filename[:-4]+"resized.jpg") #option 2
        picture.resize((500,modheight)).save(destinationfolder+"\\"+filename) #option 1
    
print('In which directory do you want to resize pictures? Provide input of the form: C:\dir1\subdir1\subdir2')
userdir = str(input())
dirfiles = os.listdir(userdir)
destinationfolder = userdir+"\\resized"
if not os.path.exists(destinationfolder): os.makedirs(destinationfolder)

failed=[]
##os.walk method; loops for all files and subdirectories
for dirpath, subdirs, files in os.walk(userdir):
    for filename in files:
        if os.path.isfile(str(dirpath) + "\\" + filename):
            absfilename = os.path.join(os.path.abspath(dirpath), filename) #option 2
        try: resizepic(filename)
        except: failed.append(absfilename)
print("Unable to convert:", failed)

##Folder only option; loops only for all files, no subdirectories
#for i in range(len(dirfiles)):
#    filename = dirfiles[i]
#    readdpath = re.compile(r'[a-zA-Z]\:\\') #re of something like "C:\\"
#    if not readdpath.search(filename): filename = os.path.join(os.getcwd(), filename) #fills in full path into filename if user lazy
#    try: resizepic(filename)
#    except: failed.append(absfilename)

print("Unable to convert:", failed)