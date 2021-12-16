import glob
import os
import exifread
import shutil
imagesDIR=input('The DIR your images in:')
targetDIR=input('The DIR your images out:')
imgnames=glob.glob(imagesDIR+"/*/*/*.jpg")
for imgname in imgnames:
    print(imgname)
    time=imgname.split("_")[2]
    if len(time)!=10:
        shutil.move(imgname,targetDIR)