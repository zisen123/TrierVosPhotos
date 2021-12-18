import os
import exifread
import shutil
import sys
import re

imagesDIR=sys.argv[1]
targetDIR=sys.argv[2]
dicOriginal={}
dicTarget={}

for path, subdirs, files in os.walk(imagesDIR):
    for name in files:
        if re.search(r'JFIF',name):
            namewithoutExt=name.split('.')[0]
            dicOriginal[namewithoutExt]=os.path.join(path, name)
for path, subdirs, files in os.walk(targetDIR):
    for name in files:
        
        namewithoutExt=name.split('.')[0]
        dicTarget[namewithoutExt]=os.path.join(path, name)

for namewithoutExt in dicOriginal.keys():
    
    if namewithoutExt in dicTarget.keys():
        if os.path.getsize(dicOriginal[namewithoutExt]) > os.path.getsize(dicOriginal[namewithoutExt]):
            print(namewithoutExt)
            if not os.path.exists(os.path.join(targetDIR,'smallerPictures')):
                os.mkdir(os.path.join(targetDIR,'smallerPictures'))
            shutil.move(dicTarget[namewithoutExt],os.path.join(targetDIR,'smallerPictures'))
            shutil.copy(dicOriginal[namewithoutExt],dicTarget[namewithoutExt])
            print('original is bigger')
        elif os.path.getsize(dicOriginal[namewithoutExt]) < os.path.getsize(dicOriginal[namewithoutExt]):
            print('original is smaller')
        else:
            print('same size')
    else:
        print('target not exists')
        date=namewithoutExt.split("_")[1]
        y=date[0:4]
        m=date[4:6]
        if not os.path.exists(os.path.join(targetDIR,y,m)):
            os.makedirs(os.path.join(targetDIR,y,m))
        shutil.copy(dicOriginal[namewithoutExt],os.path.join(targetDIR,y,m))