您好，欢迎使用我编写的python脚本，该脚本的主要功能是将您从iPhone导出的照片与影片以日期和时间的格式重命名并转移到以日期分类的文件夹中。  

此脚本不会删除任何文件，无法读取信息的照片（PNG,JPG,MOV,MP4类型，一般是网络图片和屏幕截图，手机相机拍下来的基本自带信息)会被分类存入unknow/PNG,JPG,MOV,MP4文件夹中，而无法识别的文件则会留在原来的文件夹。


### 二进制文件（app.exe或者app）使用示例

- Windows用户：
```shell
app.exe C:\Users\Sen\Documents\TrierVosPhotos C:\Users\Sen\Documents\TrierVosPhotosSorted
```

其中`C:\Users\Sen\Documents\TrierVosPhotos`是您的原始照片与影片的目录，程序会扫描这个目录下面所有文件，而`C:\Users\Sen\Documents\TrierVosPhotosSorted`是被整理后的目录。 

- Linux用户

```shell
./app /mnt/c/Users/Sen/Documents/TrierVosPhotos /mnt/c/Users/Sen/Documents/TrierVosPhotosSorted
```
其中`/mnt/c/Users/Sen/Documents/TrierVosPhotos`是您的原始照片与影片的目录，而`/mnt/c/Users/Sen/Documents/TrierVosPhotosSorted`是被整理后的目录。




------
### 如果您想使用python源代码请看下面的示例

首先安装exifread，`pip install exifread`

在运行脚本之前请确保exiftool已经被添加到了系统环境变量中，推荐使用wsl或者linux系统[安装exiftool](https://exiftool.org/install.html#Unix)。

```shell
python3 app.py /mnt/d/Library/Pictures/DCIM /mnt/d/Library/Pictures/DCIM_sorted
```
其中`/mnt/d/Library/Pictures/DCIM`是您的原始照片与影片的目录，而`/mnt/d/Library/Pictures/DCIM_sorted`是被整理后的目录。 




