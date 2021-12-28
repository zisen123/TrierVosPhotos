import sys
import os
import exifread
import exiftool
import re
import shutil
import filetype

sourceDIR=sys.argv[1]
targetDIR=sys.argv[2]

# 遍历读取源目录下的所有文件到list Files
def getFilesList(DIR):
    Files=[]
    for path, subdirs, files in os.walk(DIR):
        for name in files:
            Files.append(os.path.join(path, name))  
    return Files

# 把Files中的文件分为照片，影片，其他，照片用ExifRead处理，影片用ExifTool处理
def SortToIMGsAndVIDs(Files):
    IMGs=[]
    VIDs=[]
    for File in Files:
        if filetype.is_image(File):
            IMGs.append(File)
        elif filetype.is_video(File):
            VIDs.append(File)
        else:
            pass
    return IMGs,VIDs

# 处理冲突，如果发现同名照片（即相同照片），优先把文件大小较大的放入日期文件夹中，文件大小较小的放入samename文件夹中，若samename文件夹下有照片也发生同名冲突，那么删除较小的照片，留下较大的照片
def conflitHandle(sourceFile,targetFile):
    if not os.path.exists(os.path.join(targetDIR,'samename')):
        os.makedirs(os.path.join(targetDIR,'samename'))
    pureName=os.path.split(sourceFile)[-1]
    if os.path.getsize(sourceFile) > os.path.getsize(targetFile):
        if os.path.exists(os.path.join(targetDIR,'samename',pureName)):
            if os.path.getsize(targetFile) > os.path.getsize(os.path.join(targetDIR,'samename',pureName)):
                os.remove(os.path.join(targetDIR,'samename',pureName))
                shutil.move(targetFile,os.path.join(targetDIR,'samename',pureName))
                shutil.copy2(sourceFile,targetFile)
            else:
                os.remove(targetFile)
                shutil.copy2(sourceFile,targetFile)
        print('sourceFile is bigger')
    else:
        if os.path.exists(os.path.join(targetDIR,'samename',pureName)):
            if os.path.getsize(sourceFile) > os.path.getsize(os.path.join(targetDIR,'samename',pureName)):
                os.remove(os.path.join(targetDIR,'samename',pureName))
                shutil.copy2(sourceFile,os.path.join(targetDIR,'samename',pureName))
            else:
                os.remove(targetFile)
                shutil.copy2(sourceFile,targetFile)
        print('sourceFile is smaller')

# 使用ExifRead读取源目录下的照片中的Exif信息并以日期时间格式重命名后放入目标日期文件夹，若不存在Exif信息则传递给名称匹配函数
def renameWithIMGsExif(IMGs):
    IMGsNoExif=[]
    for IMG in IMGs:
        print(IMG)
        Ext=IMG.split('.')[-1].upper()
        with open(IMG, 'rb') as f:
            tags = exifread.process_file(f)
        if 'Image DateTime' in tags:
            DateTime=tags['Image DateTime']
            date=str(DateTime).split(" ")[0]
            time=str(DateTime).split(" ")[1]
            date=date.split(":")[0]+date.split(":")[1]+date.split(":")[2]
            time=time.split(":")[0]+time.split(":")[1]+time.split(":")[2]
            y=date[0:4]
            m=date[4:6]
            finalname='IMG_'+date+'_'+time+'.'+Ext
            if not os.path.exists(os.path.join(targetDIR,y,m)):
                os.makedirs(os.path.join(targetDIR,y,m))
            if os.path.exists(os.path.join(targetDIR,y,m,finalname)):
                conflitHandle(IMG,os.path.join(targetDIR,y,m,finalname))
            else:
                shutil.copy2(IMG,os.path.join(targetDIR,y,m,finalname))
        else:
            IMGsNoExif.append(IMG)
    return IMGsNoExif

# 使用ExifTool读取源目录下的影片中的Exif信息并以日期时间格式重命名后放入目标日期文件夹，若不存在Exif信息则传递给名称匹配函数
def renameWithVIDsExif(VIDs):
    VIDsNoExif=[]
    for VID in VIDs:
        print(VID)
        Ext=VID.split('.')[-1].upper()
        with exiftool.ExifTool() as et:
            metadata = et.get_metadata(VID)
        if 'QuickTime:CreateDate' in metadata.keys():
            DateTime=metadata['QuickTime:CreateDate']
            date=str(DateTime).split(" ")[0]
            time=str(DateTime).split(" ")[1]
            date=date.split(":")[0]+date.split(":")[1]+date.split(":")[2]
            time=time.split(":")[0]+time.split(":")[1]+time.split(":")[2]
            y=date[0:4]
            m=date[4:6]
            finalname='VID_'+date+'_'+time+'.'+Ext
            if not os.path.exists(os.path.join(targetDIR,y,m)):
                os.makedirs(os.path.join(targetDIR,y,m))
            if os.path.exists(os.path.join(targetDIR,y,m,finalname)):
                conflitHandle(VID,os.path.join(targetDIR,y,m,finalname))
            else:
                shutil.copy2(VID,os.path.join(targetDIR,y,m,finalname))
        else:
            VIDsNoExif.append(VID)
    return VIDsNoExif

# 对于没有Exif的照片和影片，名称中也许包含可能的日期时间，对其中可能的日期时间进行匹配搜索，
# 并重命名后放入unknown文件夹（这其中可能包含了被网盘软件消除了Exif的照片和影片，但是仍然是个人照片）。
# 若名称中也找不到任何信息则不做任何操作直接放入unknwon文件夹（基本是网络图片非个人图片）
def renameWithDateTimeInName(FilesNoExif):
    datetimepat1=re.compile(r'(\d{8} \d{6}|\d{8}_\d{6}|\d{8}-\d{6})')
    datetimepat2=re.compile(r'(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}|\d{4}-\d{2}-\d{2} \d{2}-\d{2}-\d{2})|\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}')
    for File in FilesNoExif:
        print(File)
        Ext=File.split('.')[-1].upper()
        if re.search(r'(\d{8} \d{6}|\d{8}_\d{6}|\d{8}-\d{6})',File):
            datetime=datetimepat1.findall(File)[0]
            date=datetime[0:8]
            time=datetime[9:15]
            y=date[0:4]
            m=date[4:6]
            if filetype.is_image(FilesNoExif[0]):
                finalname='IMG_'+date+'_'+time+'.'+Ext
            elif filetype.is_video(FilesNoExif[0]):
                finalname='VID_'+date+'_'+time+'.'+Ext
            if not os.path.exists(os.path.join(targetDIR,'unknown',Ext,y,m)):
                os.makedirs(os.path.join(targetDIR,'unknown',Ext,y,m))
            if os.path.exists(os.path.join(targetDIR,'unknown',Ext,y,m)):
                conflitHandle(File,os.path.join(targetDIR,'unknown',Ext,y,m))
            else:
                shutil.copy2(File,os.path.join(targetDIR,y,m,finalname))
        elif re.search(r'(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}|\d{4}-\d{2}-\d{2} \d{2}-\d{2}-\d{2})|\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}',File):
            datetime=datetimepat2.findall(File)[0]
            date=datetime[0:4]+datetime[5:7]+datetime[8:10]
            time=datetime[11:13]+datetime[14:16]+datetime[17:19]
            y=date[0:4]
            m=date[4:6]
            if filetype.is_image(FilesNoExif[0]):
                finalname='IMG_'+date+'_'+time+'.'+Ext
            elif filetype.is_video(FilesNoExif[0]):
                finalname='VID_'+date+'_'+time+'.'+Ext
            if not os.path.exists(os.path.join(targetDIR,'unknown',Ext,y,m)):
                os.makedirs(os.path.join(targetDIR,'unknown',Ext,y,m))
            shutil.copy2(File,os.path.join(targetDIR,'unknown',Ext,y,m,finalname))
        else:
            if not os.path.exists(os.path.join(targetDIR,'unknown',Ext)):
                os.makedirs(os.path.join(targetDIR,'unknown',Ext))
            shutil.copy2(File,os.path.join(targetDIR,'unknown',Ext))

# 也许有人会引用这个程序？
if __name__ == '__main__':
    Files=getFilesList(sourceDIR)
    IMGs,VIDs=SortToIMGsAndVIDs(Files)
    renameWithDateTimeInName(renameWithIMGsExif(IMGs))
    renameWithDateTimeInName(renameWithVIDsExif(VIDs))
