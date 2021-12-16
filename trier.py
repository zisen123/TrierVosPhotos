import glob
import os
import shutil
import exifread
imagesDIR=input('The DIR your images in:')
targetDIR=input('The DIR your images out:')
tempDIR=input('The DIR your images temp:')
imgnames=glob.glob(imagesDIR+"/IMG_*_*.jpg")
# imgnames=glob.glob(imagesDIR+"/IMG_*_*.HEIC")
vidnames=glob.glob(imagesDIR+"/VID_*_*.mp4")
# print(imgs)

for imgname in imgnames:
    #print(imgname)
    f = open(imgname, 'rb')
    tags = exifread.process_file(f)
    if 'Image Model' in tags and 'Image DateTime' in tags:
        date=imgname.split("_")[1]
        #print(date)
        y=date[0:4]
        m=date[4:6]
        d=date[6:7]
        if not os.path.exists(os.path.join(targetDIR,y)):
            os.mkdir(os.path.join(targetDIR,y))
        if not os.path.exists(os.path.join(targetDIR,y,m)):
            os.mkdir(os.path.join(targetDIR,y,m))
        shutil.move(imgname,os.path.join(targetDIR,y,m))

for vidname in vidnames:
    #print(imgname)
    date=vidname.split("_")[1]
    filename=vidname.split("/")[-1]
    #print(date)
    y=date[0:4]
    m=date[4:6]
    d=date[6:7]
    if not os.path.exists(os.path.join(targetDIR,y)):
        os.mkdir(os.path.join(targetDIR,y))
    if not os.path.exists(os.path.join(targetDIR,y,m)):
        os.mkdir(os.path.join(targetDIR,y,m))
    target=os.path.join(targetDIR,y,m,filename)
    if not os.path.exists(target):
        shutil.move(vidname,os.path.join(targetDIR,y,m))
    else:
        if os.path.getsize(vidname) > os.path.getsize(target):
            shutil.move(target,tempDIR)
            shutil.move(vidname,os.path.join(targetDIR,y,m))