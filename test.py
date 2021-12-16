from sys import path
import exifread
import time
import glob
import os
import re
import exiftool

# DIR=input('The DIR your images in:')
imagesDIR='/mnt/c/Users/Sen/Desktop/TrierDesImages'
targetDIR='/mnt/c/Users/Sen/Desktop/TrierDesImages'
offset=input('The UTC offset where you take your videos(for example if you take it in China you should type "8"):')
for path, subdirs, files in os.walk(imagesDIR):
    for name in files:
        print(name)
        if re.search(r'\.(MOV|mov)',name):
            filenamewithpath=os.path.join(path, name)
            with exiftool.ExifTool() as et:
                metadata = et.get_metadata(filenamewithpath)
            for key,value in metadata.items():
                if re.search(r'^\d{4}:\d{2}:\d{2} \d{2}:\d{2}:\d{2}',str(value)) and re.search(r'QuickTime:CreationDate',str(key)): 
                    datetime=str(value)[0:19]
                    date=str(datetime).split(" ")[0]
                    time=str(datetime).split(" ")[1]
                    date=date.split(":")[0]+date.split(":")[1]+date.split(":")[2]
                    time=time.split(":")[0]+time.split(":")[1]+time.split(":")[2]
                    y=date[0:4]
                    m=date[4:6]
                    finalname='VID_'+date+'_'+time+".MOV"
                    if not os.path.exists(os.path.join(targetDIR,y)):
                        os.mkdir(os.path.join(targetDIR,y))
                    if not os.path.exists(os.path.join(targetDIR,y,m)):
                        os.mkdir(os.path.join(targetDIR,y,m))                    
                    os.rename(filenamewithpath,os.path.join(targetDIR,y,m,finalname))
        elif re.search(r'\.(mp4|MP4)',name):
            filenamewithpath=os.path.join(path, name)
            with exiftool.ExifTool() as et:
                metadata = et.get_metadata(filenamewithpath)
                print(metadata)
            for key,value in metadata.items():
                if re.search(r'^\d{4}:\d{2}:\d{2} \d{2}:\d{2}:\d{2}',str(value)) and re.search(r'QuickTime:CreationDate',str(key)): 
                    datetime=str(value)[0:19]
                    date=str(datetime).split(" ")[0]
                    time=str(datetime).split(" ")[1]
                    date=date.split(":")[0]+date.split(":")[1]+date.split(":")[2]
                    time=time.split(":")[0]+time.split(":")[1]+time.split(":")[2]
                    y=date[0:4]
                    m=date[4:6]
                    finalname='VID_'+date+'_'+time+".MP4"
                    if not os.path.exists(os.path.join(targetDIR,y)):
                        os.mkdir(os.path.join(targetDIR,y))
                    if not os.path.exists(os.path.join(targetDIR,y,m)):
                        os.mkdir(os.path.join(targetDIR,y,m))                    
                    os.rename(filenamewithpath,os.path.join(targetDIR,y,m,finalname))                    
        elif re.search(r'\.(JPG|jpg|HEIC|heic)',name):
            filenamewithpath=os.path.join(path, name)
            with open(filenamewithpath, 'rb') as f:
                tags = exifread.process_file(f)
            print(tags)
            if 'Image Model' in tags and 'Image DateTime' in tags:
                DateTime=tags['Image DateTime']
                date=str(DateTime).split(" ")[0]
                time=str(DateTime).split(" ")[1]
                date=date.split(":")[0]+date.split(":")[1]+date.split(":")[2]
                time=time.split(":")[0]+time.split(":")[1]+time.split(":")[2]
                y=date[0:4]
                m=date[4:6]
                if re.search(r'\.(HEIC|heic)',name):
                    finalname='IMG_'+date+'_'+time+".HEIC"
                elif re.search(r'\.(JPG|jpg)',name):
                    finalname='IMG_'+date+'_'+time+".JPG"
                if not os.path.exists(os.path.join(targetDIR,y)):
                    os.mkdir(os.path.join(targetDIR,y))
                if not os.path.exists(os.path.join(targetDIR,y,m)):
                    os.mkdir(os.path.join(targetDIR,y,m))
                os.rename(filenamewithpath,os.path.join(targetDIR,y,m,finalname))






































# for path, subdirs, files in os.walk(imagesDIR):
#     for name in files:
#         if re.search(r'\.(MOV|mov)',name):
#             filenamewithpath=os.path.join(path, name)
#             with exiftool.ExifTool() as et:
#                 metadata = et.get_metadata(filenamewithpath)
#             for key,value in metadata.items():
#                 if re.search(r'^\d{4}:\d{2}:\d{2} \d{2}:\d{2}:\d{2}',str(value)) and re.search(r'QuickTime:CreationDate',str(key)): 
#                     datetime=str(value)[0:19]
#                     date=str(datetime).split(" ")[0]
#                     time=str(datetime).split(" ")[1]
#                     date=date.split(":")[0]+date.split(":")[1]+date.split(":")[2]
#                     time=time.split(":")[0]+time.split(":")[1]+time.split(":")[2]
#                     y=date[0:4]
#                     m=date[4:6]
#                     finalname='VID_'+date+'_'+time+".MOV"
#                     if not os.path.exists(os.path.join(targetDIR,y)):
#                         os.mkdir(os.path.join(targetDIR,y))
#                     if not os.path.exists(os.path.join(targetDIR,y,m)):
#                         os.mkdir(os.path.join(targetDIR,y,m))                    
#                     os.rename(filenamewithpath,os.path.join(targetDIR,y,m,finalname))
#         elif re.search(r'\.(mp4|MP4)',name):
#             filenamewithpath=os.path.join(path, name)
#             with exiftool.ExifTool() as et:
#                 metadata = et.get_metadata(filenamewithpath)
#                 print(metadata)
#             for key,value in metadata.items():
#                 if re.search(r'^\d{4}:\d{2}:\d{2} \d{2}:\d{2}:\d{2}',str(value)) and re.search(r'QuickTime:CreationDate',str(key)): 
#                     datetime=str(value)[0:19]
#                     date=str(datetime).split(" ")[0]
#                     time=str(datetime).split(" ")[1]
#                     date=date.split(":")[0]+date.split(":")[1]+date.split(":")[2]
#                     time=time.split(":")[0]+time.split(":")[1]+time.split(":")[2]
#                     y=date[0:4]
#                     m=date[4:6]
#                     finalname='VID_'+date+'_'+time+".MP4"
#                     if not os.path.exists(os.path.join(targetDIR,y)):
#                         os.mkdir(os.path.join(targetDIR,y))
#                     if not os.path.exists(os.path.join(targetDIR,y,m)):
#                         os.mkdir(os.path.join(targetDIR,y,m))                    
#                     os.rename(filenamewithpath,os.path.join(targetDIR,y,m,finalname))                    
#         if re.search(r'\.(HEIC|heic)',name):
#             filenamewithpath=os.path.join(path, name)
#             with exiftool.ExifTool() as et:
#                 metadata = et.get_metadata(filenamewithpath)
#             for key,value in metadata.items():
#                 if re.search(r'^\d{4}:\d{2}:\d{2} \d{2}:\d{2}:\d{2}',str(value)) and re.search(r'EXIF:CreateDate',str(key)): 
#                     datetime=str(value)[0:19]
#                     date=str(datetime).split(" ")[0]
#                     time=str(datetime).split(" ")[1]
#                     date=date.split(":")[0]+date.split(":")[1]+date.split(":")[2]
#                     time=time.split(":")[0]+time.split(":")[1]+time.split(":")[2]
#                     y=date[0:4]
#                     m=date[4:6]
#                     finalname='IMG_'+date+'_'+time+".HEIC"
#                     if not os.path.exists(os.path.join(targetDIR,y)):
#                         os.mkdir(os.path.join(targetDIR,y))
#                     if not os.path.exists(os.path.join(targetDIR,y,m)):
#                         os.mkdir(os.path.join(targetDIR,y,m))                    
#                     os.rename(filenamewithpath,os.path.join(targetDIR,y,m,finalname))
#         if re.search(r'\.(JPG|\.jpg)',name):
#             filenamewithpath=os.path.join(path, name)
#             with exiftool.ExifTool() as et:
#                 metadata = et.get_metadata(filenamewithpath)
#             for key,value in metadata.items():
#                 if re.search(r'^\d{4}:\d{2}:\d{2} \d{2}:\d{2}:\d{2}',str(value)) and re.search(r'EXIF:CreateDate',str(key)): 
#                     datetime=str(value)[0:19]
#                     date=str(datetime).split(" ")[0]
#                     time=str(datetime).split(" ")[1]
#                     date=date.split(":")[0]+date.split(":")[1]+date.split(":")[2]
#                     time=time.split(":")[0]+time.split(":")[1]+time.split(":")[2]
#                     y=date[0:4]
#                     m=date[4:6]
#                     finalname='IMG_'+date+'_'+time+".JPG"
#                     if not os.path.exists(os.path.join(targetDIR,y)):
#                         os.mkdir(os.path.join(targetDIR,y))
#                     if not os.path.exists(os.path.join(targetDIR,y,m)):
#                         os.mkdir(os.path.join(targetDIR,y,m))                    
#                     os.rename(filenamewithpath,os.path.join(targetDIR,y,m,finalname)) 



























# for path, subdirs, files in os.walk(imagesDIR):
#     for name in files:
#         filenamewithpath=os.path.join(path, name)
#         with exiftool.ExifTool() as et:
#             metadata = et.get_metadata(filenamewithpath)
#         for key,value in metadata.items():
        
#             if re.search(r'^\d{4}:\d{2}:\d{2} \d{2}:\d{2}:\d{2}$',str(value)) and re.search(r'CreationDate',str(key)):
#                 datetime=str(value)
#                 date=str(datetime).split(" ")[0]
#                 time=str(datetime).split(" ")[1]
#                 time=time.split('+')[0]
#                 date=date.split(":")[0]+date.split(":")[1]+date.split(":")[2]
#                 time=time.split(":")[0]+time.split(":")[1]+time.split(":")[2]
#                 y=date[0:4]
#                 m=date[4:6]
#                 if re.search(r'\.MOV',name):
#                     name='VID_'+date+'_'+time+".MOV"
#                 if re.search(r'\.HEIC',name):
#                     name='IMG_'+date+'_'+time+".HEIC"
#                 if re.search(r'\.JPG',name):
#                     name='IMG_'+date+'_'+time+".JPG"
#                 if not os.path.exists(os.path.join(targetDIR,y)):
#                     os.mkdir(os.path.join(targetDIR,y))
#                 if not os.path.exists(os.path.join(targetDIR,y,m)):
#                     os.mkdir(os.path.join(targetDIR,y,m))
#                 os.rename(filenamewithpath,os.path.join(targetDIR,y,m,name))















# for path, subdirs, files in os.walk(imagesDIR):
#     for name in files:



#         if re.search(r'.JPG',name):
#             vidname=os.path.join(path, name)
#             with exiftool.ExifTool() as et:
#                 metadata = et.get_metadata(vidname)
#             for d in metadata:
#                 print("{:20.20} {:20.20}".format(d["SourceFile"],d["EXIF:DateTimeOriginal"]))



#             # print(metadata)
            # for key,value in metadata.items():
        
            #     if re.search(r'^\d{4}:\d{2}:\d{2} \d{2}:\d{2}:\d{2}',str(value)) and re.search(r'Creat[a-z]*Date',str(key)):
            #         datetime=str(value)[0:19]
            #         print(datetime)
                    # print(value.split('+')[0])
                
        




# listoffiles=os.walk('.')
# print(type(listoffiles))

# print(os.listdir(path='.'))


# imagesDIR=input('The DIR your images in:')
# vidnames=glob.glob(imagesDIR+"/*/*/*.MOV")
# for vidname in vidnames:
#     with exiftool.ExifTool() as et:
#         metadata = et.get_metadata(vidname)
#     if 'QuickTime:CreationDate' in metadata:
#         datetime=metadata['QuickTime:CreationDate']
#         print(type(datetime))
#         date=str(datetime).split(" ")[0]
#         time=str(datetime).split(" ")[1]
#         time=time.split('+')[0]
#         date=date.split(":")[0]+date.split(":")[1]+date.split(":")[2]
#         time=time.split(":")[0]+time.split(":")[1]+time.split(":")[2]
#         y=date[0:4]
#         m=date[4:6]
#         name='VID_'+date+'_'+time+".MOV"
#         print(name)



# with exiftool.ExifTool() as et:
#     metadata = et.get_metadata(files)
#     datetime=(metadata['QuickTime:CreationDate'])
#     date=date.split(":")[0]+date.split(":")[1]+date.split(":")[2]
#     time=time.split(":")[0]+time.split(":")[1]+time.split(":")[2]
#     y=date[0:4]
#     m=date[4:6]
# for d in metadata:

    # print("{:20.20} {:20.20}".format(d["SourceFile"], d["EXIF:DateTimeOriginal"]))

# datetime=time.strftime('%Y%m%d_%H%M%S', time.localtime(os.path.getctime('./IMG_2390.MOV')))
# print(datetime)
# print(type(datetime))
# print(datetime.split('_')[0])

# f = open('IMG_2495.MOV', 'rb')

# tags = exifread.process_file(f)
# print(tags)
# if 'Image Model' in tags and 'Image DateTime' in tags:
#     print(tags['Image Model'],tags['Image DateTime'])