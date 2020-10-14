# 树莓派极简安装OpenCv

我用的环境：
树莓派3b+
Python3.5.4
树莓派官方操作系统
以下是安装步骤：
树莓派相关库安装：
sudo apt-get update
sudo apt-get install libjpeg-dev
sudo apt-get install libatlas-base-dev
sudo apt-get install libjpeg-dev
sudo apt-get install libtiff5-dev
sudo apt-get install libpng12-dev
sudo apt-get install libqtgui4 libqt4-test
sudo apt-get install libjasper-dev

OpenCV模块pip安装
sudo pip3 install opencv-python

安装完成
————————————————
版权声明：本文为CSDN博主「小宋是呢」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/xiaosongshine/article/details/83095954



# cannot connect to X server报错处理方法：

原因是xshell没有设置: 主机右击->属性->隧道->转发x11连接到xmanager, 就能成功调用图形界面了;