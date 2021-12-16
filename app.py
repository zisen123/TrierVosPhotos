import glob
import os
import re
import time
import exiftool
import exifread
import sys
import shutil
imagesDIR=sys.argv[1]
targetDIR=sys.argv[2]

unknow='unknow'
heic='HEIC'
jpg='JPG'
filenamewithpaths=[]
for path, subdirs, files in os.walk(imagesDIR):
    for name in files:
        filenamewithpaths.append(os.path.join(path, name))
for filenamewithpath in filenamewithpaths:  
    name=filenamewithpath  
    print(name)
    if re.search(r'\.(MOV|mov)',name):
        with exiftool.ExifTool() as et:
            metadata = et.get_metadata(filenamewithpath)
        if 'QuickTime:CreationDate' in metadata.keys():
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
                    # if not os.path.exists(os.path.join(targetDIR,y)):
                    #     os.mkdir(os.path.join(targetDIR,y))                     
                    if not os.path.exists(os.path.join(targetDIR,y,m)):
                        os.mkdir(os.path.join(targetDIR,y,m))    
                    try:            
                        os.rename(filenamewithpath,os.path.join(targetDIR,y,m,finalname))
                    except Exception as e:
                        pass
        else:
            if not os.path.exists(os.path.join(targetDIR,'unknow','MOV')):
                os.mkdir(os.path.join(targetDIR,'unknow','MOV'))
            try:
                shutil.move(filenamewithpath,os.path.join(targetDIR,'unknow','MOV'))                    
            except Exception:
                pass  
    # elif re.search(r'\.(mp4|MP4)',name):
    #     filenamewithpath=os.path.join(path, name)
    #     with exiftool.ExifTool() as et:
    #         metadata = et.get_metadata(filenamewithpath)
    #         print(metadata)
    #     for key,value in metadata.items():
    #         if re.search(r'^\d{4}:\d{2}:\d{2} \d{2}:\d{2}:\d{2}',str(value)) and re.search(r'QuickTime:CreationDate',str(key)): 
    #             datetime=str(value)[0:19]
    #             date=str(datetime).split(" ")[0]
    #             time=str(datetime).split(" ")[1]
    #             date=date.split(":")[0]+date.split(":")[1]+date.split(":")[2]
    #             time=time.split(":")[0]+time.split(":")[1]+time.split(":")[2]
    #             y=date[0:4]
    #             m=date[4:6]
    #             finalname='VID_'+date+'_'+time+".MP4"
    #             if not os.path.exists(os.path.join(targetDIR,y)):
    #                 os.mkdir(os.path.join(targetDIR,y))
    #             if not os.path.exists(os.path.join(targetDIR,y,m)):
    #                 os.mkdir(os.path.join(targetDIR,y,m))                    
    #             os.rename(filenamewithpath,os.path.join(targetDIR,y,m,finalname))                    
    elif re.search(r'\.(JPG|jpg|HEIC|heic)',name):
        with open(filenamewithpath, 'rb') as f:
            tags = exifread.process_file(f)
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
        else:
            if re.search(r'\.(HEIC|heic)',name):
                if not os.path.exists(os.path.join(targetDIR,unknow,heic)):
                    os.mkdir(os.path.join(targetDIR,unknow,heic))
                try:
                    shutil.move(filenamewithpath,os.path.join(targetDIR,unknow,heic))                    
                except Exception:
                    pass                        
                
            elif re.search(r'\.(JPG|jpg)',name):
                if not os.path.exists(os.path.join(targetDIR,unknow,jpg)):
                    print(os.path.join(targetDIR,unknow,jpg))
                    targetpath=os.path.join(targetDIR,unknow,jpg)
                    os.makedirs(targetpath)
                try:
                    shutil.move(filenamewithpath,os.path.join(targetDIR,unknow,jpg))                    
                except Exception:
                    pass
    elif re.search(r'\.(JPEG|jpeg)',name):
        if not os.path.exists(os.path.join(targetDIR,'unknow','JPEG')):
            os.mkdir(os.path.join(targetDIR,'unknow','JPEG'))
        try:
            shutil.move(filenamewithpath,os.path.join(targetDIR,'unknow','JPEG'))                    
        except Exception:
            pass                    
    elif re.search(r'\.(mp4|MP4)',name):
        
        if not os.path.exists(os.path.join(targetDIR,'unknow','MP4')):
            os.mkdir(os.path.join(targetDIR,'unknow','MP4'))
        try:
            shutil.move(filenamewithpath,os.path.join(targetDIR,'unknow','MP4')) 
        except:
            pass                       
    elif re.search(r'\.(png|PNG)',name):
        
        if not os.path.exists(os.path.join(targetDIR,'unknow','PNG')):
            os.mkdir(os.path.join(targetDIR,'unknow','PNG'))
        try:
            shutil.move(filenamewithpath,os.path.join(targetDIR,'unknow','PNG')) 
        except:
            pass
    else:
        pass























            # if not os.path.exists(os.path.join(targetDIR,'unknow','OTHERTYPE')):
            #     os.mkdir(os.path.join(targetDIR,'unknow','OTHERTYPE'))
            # try:
            #     shutil.move(filenamewithpath,os.path.join(targetDIR,'unknow','OTHERTYPE'))
            # except Exception:
            #     pass
            








            # filenamewithpath=os.path.join(path, name)
            # with exiftool.ExifTool() as et:
            #     metadata = et.get_metadata(filenamewithpath)
            # for key,value in metadata.items():
            #     if re.search(r'^\d{4}:\d{2}:\d{2} \d{2}:\d{2}:\d{2}',str(value)) and re.search(r'EXIF:CreateDate',str(key)): 
            #         datetime=str(value)[0:19]
            #         date=str(datetime).split(" ")[0]
            #         time=str(datetime).split(" ")[1]
            #         date=date.split(":")[0]+date.split(":")[1]+date.split(":")[2]
            #         time=time.split(":")[0]+time.split(":")[1]+time.split(":")[2]
            #         y=date[0:4]
            #         m=date[4:6]
            #         finalname='IMG_'+date+'_'+time+".JPG"
            #         if not os.path.exists(os.path.join(targetDIR,y)):
            #             os.mkdir(os.path.join(targetDIR,y))
            #         if not os.path.exists(os.path.join(targetDIR,y,m)):
            #             os.mkdir(os.path.join(targetDIR,y,m))                    
            #         os.rename(filenamewithpath,os.path.join(targetDIR,y,m,finalname)) 



































# '''                    
# # vidnames=glob.glob(imagesDIR+"/*/*/*")
# for path, subdirs, files in os.walk(imagesDIR):
#     for name in files:
        
#         if re.search(r'\.MOV',name):
#             filenamewithpath=os.path.join(path, name)
#             with exiftool.ExifTool() as et:
#                 metadata = et.get_metadata(filenamewithpath)
#             for key,value in metadata.items():
#                 if re.search(r'^\d{4}:\d{2}:\d{2} \d{2}:\d{2}:\d{2}',str(value)) and re.search(r'Creat[a-z]*Date',str(key)): 
#                     datetime=str(value)[0:19]
#                     date=str(datetime).split(" ")[0]
#                     time=str(datetime).split(" ")[1]
#                     date=date.split(":")[0]+date.split(":")[1]+date.split(":")[2]
#                     time=time.split(":")[0]+time.split(":")[1]+time.split(":")[2]
#                     y=date[0:4]
#                     m=date[4:6]
#                     finalname='VID_'+date+'_'+time+".MOV"
#                     os.rename(filenamewithpath,os.path.join(targetDIR,y,m,finalname))
#         if re.search(r'\.HEIC',name):
#             filenamewithpath=os.path.join(path, name)
#             with exiftool.ExifTool() as et:
#                 metadata = et.get_metadata(filenamewithpath)
#             for key,value in metadata.items():
#                 if re.search(r'^\d{4}:\d{2}:\d{2} \d{2}:\d{2}:\d{2}',str(value)) and re.search(r'Creat[a-z]*Date',str(key)): 
#                     datetime=str(value)[0:19]
#                     date=str(datetime).split(" ")[0]
#                     time=str(datetime).split(" ")[1]
#                     date=date.split(":")[0]+date.split(":")[1]+date.split(":")[2]
#                     time=time.split(":")[0]+time.split(":")[1]+time.split(":")[2]
#                     y=date[0:4]
#                     m=date[4:6]
#                     finalname='IMG_'+date+'_'+time+".HEIC"
#                     os.rename(filenamewithpath,os.path.join(targetDIR,y,m,finalname))
#         if re.search(r'\.JPG',name):
#             filenamewithpath=os.path.join(path, name)
#             with exiftool.ExifTool() as et:
#                 metadata = et.get_metadata(filenamewithpath)
#             for key,value in metadata.items():
#                 if re.search(r'^\d{4}:\d{2}:\d{2} \d{2}:\d{2}:\d{2}',str(value)) and re.search(r'Creat[a-z]*Date',str(key)): 
#                     datetime=str(value)[0:19]
#                     date=str(datetime).split(" ")[0]
#                     time=str(datetime).split(" ")[1]
#                     date=date.split(":")[0]+date.split(":")[1]+date.split(":")[2]
#                     time=time.split(":")[0]+time.split(":")[1]+time.split(":")[2]
#                     y=date[0:4]
#                     m=date[4:6]
#                     finalname='IMG_'+date+'_'+time+".JPG"
#                     os.rename(filenamewithpath,os.path.join(targetDIR,y,m,finalname))   



#         if re.search(r'\.HEIC',name):
#             name='IMG_'+date+'_'+time+".HEIC"
#         if re.search(r'\.JPG',name):
#             name='IMG_'+date+'_'+time+".JPG"
#         if not os.path.exists(os.path.join(targetDIR,y)):
#             os.mkdir(os.path.join(targetDIR,y))
#         if not os.path.exists(os.path.join(targetDIR,y,m)):
#             os.mkdir(os.path.join(targetDIR,y,m))
#         os.rename(filenamewithpath,os.path.join(targetDIR,y,m,finalname))

#         # if re.search(r'^\d{4}:\d{2}:\d{2} \d{2}:\d{2}:\d{2}',str(value)) and re.search(r'Creat[a-z]*Date',str(key)):
#         #     datetime=str(value)[0:19]
#         #     date=str(datetime).split(" ")[0]
#         #     time=str(datetime).split(" ")[1]
#         #     date=date.split(":")[0]+date.split(":")[1]+date.split(":")[2]
#         #     time=time.split(":")[0]+time.split(":")[1]+time.split(":")[2]
#         #     y=date[0:4]
#         #     m=date[4:6]
# '''                
















        # print(os.path.join(path, name))
        # if re.search(r'.MOV',name):
        #     vidname=os.path.join(path, name)
        #     with exiftool.ExifTool() as et:
        #         metadata = et.get_metadata(vidname)
        #     if 'QuickTime:CreationDate' in metadata:
        #         datetime=str(metadata['QuickTime:CreationDate'])
        #         date=str(datetime).split(" ")[0]
        #         time=str(datetime).split(" ")[1]
        #         time=time.split('+')[0]
        #         date=date.split(":")[0]+date.split(":")[1]+date.split(":")[2]
        #         time=time.split(":")[0]+time.split(":")[1]+time.split(":")[2]
        #         y=date[0:4]
        #         m=date[4:6]
        #         name='VID_'+date+'_'+time+".MOV"
        #         if not os.path.exists(os.path.join(targetDIR,y)):
        #             os.mkdir(os.path.join(targetDIR,y))
        #         if not os.path.exists(os.path.join(targetDIR,y,m)):
        #             os.mkdir(os.path.join(targetDIR,y,m))
        #         os.rename(vidname,os.path.join(targetDIR,y,m,name))




# for vidname in vidnames:
#     with exiftool.ExifTool() as et:
#         metadata = et.get_metadata(vidname)
#     if 'QuickTime:CreationDate' in metadata:
#         datetime=str(metadata['QuickTime:CreationDate'])
#         date=str(datetime).split(" ")[0]
#         time=str(datetime).split(" ")[1]
#         time=time.split('+')[0]
#         date=date.split(":")[0]+date.split(":")[1]+date.split(":")[2]
#         time=time.split(":")[0]+time.split(":")[1]+time.split(":")[2]
#         y=date[0:4]
#         m=date[4:6]
#         name='VID_'+date+'_'+time+".MOV"
#         if not os.path.exists(os.path.join(targetDIR,y)):
#             os.mkdir(os.path.join(targetDIR,y))
#         if not os.path.exists(os.path.join(targetDIR,y,m)):
#             os.mkdir(os.path.join(targetDIR,y,m))
#         os.rename(vidname,os.path.join(targetDIR,y,m,name))



# imgnames=glob.glob(imagesDIR+"/*/*.HEIC")
# for imgname in imgnames:
#     f = open(imgname, 'rb')
#     tags = exifread.process_file(f)
#     if 'Image Model' in tags and 'Image DateTime' in tags:
#         DateTime=tags['Image DateTime']
#         date=str(DateTime).split(" ")[0]
#         time=str(DateTime).split(" ")[1]
#         date=date.split(":")[0]+date.split(":")[1]+date.split(":")[2]
#         time=time.split(":")[0]+time.split(":")[1]+time.split(":")[2]
#         y=date[0:4]
#         m=date[4:6]
#         name='IMG_'+date+'_'+time+".HEIC"
#         if not os.path.exists(os.path.join(targetDIR,y)):
#             os.mkdir(os.path.join(targetDIR,y))
#         if not os.path.exists(os.path.join(targetDIR,y,m)):
#             os.mkdir(os.path.join(targetDIR,y,m))
#         os.rename(imgname,os.path.join(targetDIR,y,m,name))

# imgnames=glob.glob(imagesDIR+"/*/*.JPG")
# for imgname in imgnames:
#     f = open(imgname, 'rb')
#     tags = exifread.process_file(f)
#     if 'Image Model' in tags and 'Image DateTime' in tags:
#         DateTime=tags['Image DateTime']
#         date=str(DateTime).split(" ")[0]
#         time=str(DateTime).split(" ")[1]
#         date=date.split(":")[0]+date.split(":")[1]+date.split(":")[2]
#         time=time.split(":")[0]+time.split(":")[1]+time.split(":")[2]
#         y=date[0:4]
#         m=date[4:6]
#         name='IMG_'+date+'_'+time+".JPG"
#         if not os.path.exists(os.path.join(targetDIR,y)):
#             os.mkdir(os.path.join(targetDIR,y))
#         if not os.path.exists(os.path.join(targetDIR,y,m)):
#             os.mkdir(os.path.join(targetDIR,y,m))
#         os.rename(imgname,os.path.join(targetDIR,y,m,name))

# vidnames=glob.glob(imagesDIR+"/*/*/*.MOV")
# for vidname in vidnames:
#     datetime=time.strftime('%Y%m%d_%H%M%S', time.localtime(os.path.getctime(vidname)))

# imgnames=glob.glob(imagesDIR+"/*/*/*_*_*_*.jpg")
# for imgname in imgnames:
#     pre=imgname.split("_")[0]
#     date=imgname.split("_")[1]
#     time=imgname.split("_")[2]
#     print(pre+"_"+date+"_"+time+".jpg")
#     os.rename(imgname,pre+"_"+date+"_"+time+".jpg")



# imgnames=glob.glob(imagesDIR+"/*/*/MVIMG_*_*.jpg")
# for imgname in imgnames:
#     rest=imgname.split("_")[1]+"_"+imgname.split("_")[2]
#     os.rename(imgname,imagesDIR+"/IMG_"+rest)

# imgnames=[f for f in glob.glob(imagesDIR+"/*/*/*") if re.search(r'.IMG\d{14}.jpg$',f)]
# for imgname in imgnames:
#     datetime=imgname.split("IMG")[1]
#     date=datetime[0:8]
#     time=datetime[8:]
#     os.rename(imgname,imagesDIR+"/IMG_"+date+"_"+time)




# imgnames=glob.glob(imagesDIR+"/*/*/*.MP4")
# for imgname in imgnames:
#     filename=imgname.split(".")[0]
#     print(filename)
#     os.rename(imgname,filename+".mp4")

# imgnames=glob.glob(imagesDIR+"/*/*/*.MOV")
# for imgname in imgnames:
#     filename=imgname.split(".")[0]
#     print(filename)
#     os.rename(imgname,filename+".mov")

#     imgnames=glob.glob(imagesDIR+"/*/*/*.PNG")
# for imgname in imgnames:
#     filename=imgname.split(".")[0]
#     print(filename)
#     os.rename(imgname,filename+".png")

# imgnames=glob.glob(imagesDIR+"/IMG*.jpg")
# for imgname in imgnames:
#     date=imgname.split("_")[1]
#     time=imgname.split("_")[2]
#     if len(date)==6:
#         date=date+time[:2]
#         time=time[2:]
#         os.rename(imgname,imagesDIR+"/IMG_"+date+"_"+time)



# imgnames=[f for f in glob.glob(imagesDIR+"/*/*/video*.mp4") if re.search(r'.video_\d{8}_\d{6}.mp4$',f)]
# for imgname in imgnames:
#     date=imgname.split("_")[1]
#     time=imgname.split("_")[2]
#     os.rename(imgname,imagesDIR+"/VID_"+date+"_"+time)

