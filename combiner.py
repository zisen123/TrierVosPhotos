import glob
import os
import exifread
import shutil
imagesDIR=input('The DIR your images in:')
targetDIR=input('The DIR your images out:')
imgnames=glob.glob(imagesDIR+"/*/*/*.jpg")
imgnames1=glob.glob(targetDIR+"/*/*/*.jpg")
for imgname in imgnames:
    imgname1=imgname
    
    date=imgname.split("_")[1]
    
    #print(date)
    y=date[0:4]
    m=date[4:6]
    d=date[6:7]
    


    
    shutil.move(imgname,os.path.join(targetDIR,y,m))


    # f = open(imgname, 'rb')

    # # Return Exif tags
    # tags = exifread.process_file(f)
    # if 'Image Model' not in tags:
    #     shutil.move(imgname,targetDIR)