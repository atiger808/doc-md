#### 链接OpenCV4 到自己的Python3

1. 虚拟环境目录，让我们创建一个软链接 从OpenCV的系统安装包site-packages

```
$ cd ~/.virtualenvs/cv/lib/python3.5/site-packages/   #进入虚拟环境目录
# 创建OpenCV目录下的cv2.cpython-35m-arm-linux-gnueabihf.so文件的软链接cv2.o
$ ln -s /usr/local/python/cv2/python-3.5/cv2.cpython-35m-arm-linux-gnueabihf.so cv2.so 
```

2. 链接到本地的python3

```
$ cd /usr/lib/python3/dist-packages   #进人本地python3目录
# 创建OpenCV目录下的cv2.cpython-35m-arm-linux-gnueabihf.so文件的软链接cv2.o
$ ln -s /usr/local/python/cv2/python-3.5/cv2.cpython-35m-arm-linux-gnueabihf.so cv2.so 
```

##### libQtTest.so.4: cannot open shared object file: No such file or directory 报错处理：

```
sudo apt install libqt4-test
```



#### 第22章  Web编程

##### 22.1.1 安装 Apache Web服务器

Apache服务器可以从Debian的源中下载。可以用apt下载。

首先要更新apt的软件列表。如果不运行sudo apt-get updata的话，apt软件就不知道有没有新的软件包或者版本更新。

Apache可以用下面的命令来安装

```
sudo apt-get install apache2
```

启动和停止Apacge 服务器命令：

```
sudo service apache2 start
sudo service apache2 stop
```

