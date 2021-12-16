import exifread
import glob
import os
imagesDIR=input('The DIR your images in:')
imgnames=glob.glob(imagesDIR+"/*/*/*.jpg")
for imgname in imgnames:
    # Open image file for reading (binary mode)
    f = open(imgname, 'rb')

    # Return Exif tags
    tags = exifread.process_file(f)
    if 'Image Model' in tags and 'Image DateTime' in tags:
        
        DateTime=tags['Image DateTime']
        date=str(DateTime).split(" ")[0]
        time=str(DateTime).split(" ")[1]
        date=date.split(":")[0]+date.split(":")[1]+date.split(":")[2]
        time=time.split(":")[0]+time.split(":")[1]+time.split(":")[2]
        os.rename(imgname,imagesDIR+"/IMG"+"_"+date+"_"+time+".jpg")


# print(tags['Image Model'],tags['Image DateTime'])