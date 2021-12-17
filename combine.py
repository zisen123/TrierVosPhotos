import glob
import os
import exifread
import shutil
import sys
import re

imagesDIR=sys.argv[1]
targetDIR=sys.argv[2]

# filenamewithpathsOriginal=[]
# filenamewithpathsTarget=[]
# originalName=[]
# targetName=[]
dicOriginal={}
dicTarget={}
for path, subdirs, files in os.walk(imagesDIR):
    for name in files:
        # filenamewithpathsOriginal.append(os.path.join(path, name))
        # originalName.append(name)
        dicOriginal[name]=os.path.join(path, name)
for path, subdirs, files in os.walk(targetDIR):
    for name in files:
        # filenamewithpathsTarget.append(os.path.join(path, name)) 
        # targetName.append(name)   
        dicTarget[name]=os.path.join(path, name)
print(dicTarget.keys())
for name in dicOriginal.keys():
    print(name)
    
    if name in dicTarget.keys():
        namewithpathO=dicOriginal[name]
        namewithpathT=dicTarget[name]
        sizeO=os.path.getsize(namewithpathO)
        sizeT=os.path.getsize(namewithpathT)
        print(namewithpathO)
        print(sizeO)
        print(namewithpathT)
        print(sizeT)
        if sizeO > sizeT:
            print(name)
            if not os.path.exists(os.path.join(targetDIR,'smallerPictures')):
                os.mkdir(os.path.join(targetDIR,'smallerPictures'))
            shutil.move(dicTarget[name],os.path.join(targetDIR,'smallerPictures'))
            shutil.copy(dicOriginal[name],dicTarget[name])
            print('original is bigger')
        elif os.stat(dicOriginal[name]).st_size < os.stat(dicTarget[name]).st_size:
            print('original is smaller')
        else:
            print('same size')
    else:
        print('target not exists')


        # print('target not exists')

        # date=name.split("_")[1]
        # y=date[0:4]
        # m=date[4:6]
        # d=date[6:7]
        # if not os.path.exists(os.path.join(targetDIR,y,m)):
        #     os.makedirs(os.path.join(targetDIR,y,m))
        # shutil.copy(dicOriginal[name],os.path.join(targetDIR,y,m))

        # re.search(r'^(IMG|VID)_\d{8}_\d{6}',name)















# imgnames=glob.glob(imagesDIR+"/*/*/*.jpg")
# imgnames1=glob.glob(targetDIR+"/*/*/*.jpg")
# for imgname in imgnames:
#     imgname1=imgname
    
#     date=imgname.split("_")[1]
    
#     #print(date)
#     y=date[0:4]
#     m=date[4:6]
#     d=date[6:7]
    


    
#     shutil.move(imgname,os.path.join(targetDIR,y,m))


    # f = open(imgname, 'rb')

    # # Return Exif tags
    # tags = exifread.process_file(f)
    # if 'Image Model' not in tags:
    #     shutil.move(imgname,targetDIR)