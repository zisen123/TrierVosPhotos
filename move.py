import glob
import os
import exifread
import shutil
imagesDIR=input('The DIR your images in:')
targetDIR=input('The DIR your images out:')
imgnames=glob.glob(imagesDIR+"/*/*/*.jpg")
for imgname in imgnames:
    f = open(imgname, 'rb')

    # Return Exif tags
    tags = exifread.process_file(f)
    if 'Image Model' not in tags:
        shutil.move(imgname,targetDIR)