import sys
import os
import re
imagesDIR=sys.argv[1]
# targetDIR=sys.argv[2]
filenamewithpaths=[]
for path, subdirs, files in os.walk(imagesDIR):
    for name in files:
        filenamewithpaths.append(os.path.join(path, name))
for filenamewithpath in filenamewithpaths: 
    print(filenamewithpath) 
    Newfilenamewithpath=filenamewithpath.split('.')[0]+'.JFIF'
    try:
        os.rename(filenamewithpath,Newfilenamewithpath)
    except:
        pass
























    # if re.search(r'\.(MOV|mov)',name):
    #     Newfilenamewithpath=filenamewithpath.split('.')[0]+'.MOV'
    # elif re.search(r'\.(jpg|JPG)',name):
    #     Newfilenamewithpath=filenamewithpath.split('.')[0]+'.jpg'
    # elif re.search(r'\.(mp4|MP4)',name):
    #     Newfilenamewithpath=filenamewithpath.split('.')[0]+'.MP4'
    # elif re.search(r'\.(png|PNG)',name):
    #     Newfilenamewithpath=filenamewithpath.split('.')[0]+'.PNG'                
    # elif re.search(r'\.(jpeg|JPEG)',name):
    #     Newfilenamewithpath=filenamewithpath.split('.')[0]+'.JPEG'        
    # os.rename(filenamewithpath,)