import sys
import exifread
import time
import glob
import os
import re
import shutil
import exiftool
import filetype


# a=1
# print('{a}=1')
















shutil.copy2('/mnt/c/Users/Sen/Documents/TrierVosPhotos/VID_20211203_204014.MOV','/mnt/c/Users/Sen/Documents/TargetImages/2021/12/')








""" 
sourceDIR=input('sourceDIR:')
targetDIR=input('targetDIR:')
 """



""" def getFilesList(DIR):
    Files=[]
    for path, subdirs, files in os.walk(DIR):
        for name in files:
            Files.append(os.path.join(path, name))  
    return Files

def SortToIMGsAndVIDs(Files):
    IMGs=[]
    VIDs=[]
    for File in Files:
        if filetype.is_image(File):
            IMGs.append(File)
        elif filetype.is_video(File):
            VIDs.append(File)
    return IMGs,VIDs    

IMGs,VIDs=SortToIMGsAndVIDs(getFilesList(sourceDIR))
print(IMGs)
print(VIDs) """