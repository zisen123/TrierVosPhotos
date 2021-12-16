您好，欢迎使用我编写的python脚本，该脚本的主要功能是将您从iPhone导出的照片与影片以日期和时间的格式重命名并转移到以日期分类的文件夹中。  


使用示例


```shell
python3 app.py /mnt/d/Library/Pictures/DCIM /mnt/d/Library/Pictures/DCIM_sorted
```
其中`/mnt/d/Library/Pictures/DCIM`是您的原始照片与影片的目录，而`/mnt/d/Library/Pictures/DCIM_sorted`是被整理后的目录。 

首先安装exifread，`pip install exifread`
在运行脚本之前请确保exiftool已经被添加到了系统环境变量中，推荐使用wsl或者linux系统[安装exiftool](https://exiftool.org/install.html#Unix)。


此脚本不会删除任何文件，无法读取信息的照片（PNG,JPG,MOV,MP4类型)会被分类存入unknow文件夹中，而无法识别的文件则会留在原来的文件夹。
