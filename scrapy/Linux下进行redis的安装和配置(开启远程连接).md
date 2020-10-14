# Linux下进行redis的安装和配置(开启远程连接)



1. 什么是redis?
  1.1 核心概念
  Redis是用C语言开发的高性能的键值对存储的非关系数据库。Redis存储的数据类型有以下几种：字符(String)、散列(Hash)、列表(List)、集合(Set)、有序集合(ZSet)

1.2 历史发展
2008年，意大利的一家创业公司Merzia推出了一款基于MySQL的网站实时统计系统LLOOGG，然而没过多久该公司的创始人 Salvatore Sanfilippo便对MySQL的性能感到失望，于是他决定亲自为LLOOGG量身定做一个数据库，并于2009年开发完成，这个数据库就是Redis。 不过Salvatore Sanfilippo并不满足只将Redis用于LLOOGG这一款产品，而是希望更多的人使用它，于是在同一年Salvatore Sanfilippo将Redis开源发布，并开始和Redis的另一名主要的代码贡献者Pieter Noordhuis一起继续着Redis的开发，直到今天。
  SalvatoreSanfilippo自己也没有想到，短短的几年时间，Redis就拥有了庞大的用户群体。HackerNews在2012年发布了一份数据库的使用情况调查，结果显示有近12%的公司在使用Redis。国内如新浪微博、街旁网、知乎网，国外如GitHub、Stack Overflow、Flickr等都是Redis的用户。
  VMware公司从2010年开始赞助Redis的开发， Salvatore Sanfilippo和Pieter Noordhuis也分别在3月和5月加入VMware，全职开发Redis。

1.3 redis的应用场景
缓存（数据查询、短连接、新闻内容、商品内容等等）。（最多使用）
分布式集群架构中的session分离。
聊天室的在线好友列表。
任务队列。（秒杀、抢购、12306等等）
应用排行榜。
网站访问统计。
数据过期处理（可以精确到毫秒）
2.redis在linux下的安装
2.1 安装
#安装C语言环境(已经安装可跳过)
yum install gcc-c++
#下载压缩包
wget http://download.redis.io/releases/redis-4.0.1.tar.gz
#解压
tar -zxvf redis-4.0.1.tar.gz
#进入解压目录并编译Redis
cd redis-4.0.1
#进行编译
make
#安装Redis
make install PREFIX=/usr/local/redis
1
2
3
4
5
6
7
8
9
10
11
12
PREFIX后面的/usr/local/redis是安装路径，我们启动redis的文件都在这里，也可以自定义。
出现如下提示则安装成功：

make[1]: Entering directory `/root/redis-3.0.6/src'

Hint: It's a good idea to run 'make test' ;)

    INSTALL install
    INSTALL install
    INSTALL install
    INSTALL install
    INSTALL install
make[1]: Leaving directory `/root/redis-3.0.6/src
1
2
3
4
5
6
7
8
9
10
2.2拷贝配置文件并运行
接下把我们的配置文件redis.conf手动拷贝到安装路径,，以便开启后台运行与远程访问。

#拷贝redis.conf文件
cp -r redis.conf /usr/local/redis/bin/
1
2
安装路径下的bin目录结构


好了 现在我们可以输入命令来运行redis了

#开启服务端
./redis-server redis.conf
1
2
成功提示如下


#开启新的窗口，运行客户端进行连接
cd /usr/redis/
#链接此redis
./redis-cli  或者  ./redis-cli -h 127.0.0.1 -p 6379
1
2
3
4
-h：指定主机IP
-p：指定主机端口
默认主机IP是127.0.0.1 默认端口 6379
不填则使用默认值

成功并进行如下测试


但不可能每次都开两个窗口，我们需要配置后台运行；同时我们用程序连接也需要远程连接，接下来我们进行设置。

2.3 设置后台运行和远程连接
接下里我们在配置文件redis.conf中进行相关的配置

#打开配置文件
vim redis.conf
1
2
在vim编辑模式下，输入行数+gg可以快捷跳行。例如跳到第138行，输入：138gg

2.3.1 设置后台启动
将第138行的daemonize no修改为daemonize yes即可


2.3.2 开启远程访问
将第70行的bind注释，第90行将protected-mode改为no


2.3.3 设置密码
取消第502行的注释，并修改密码


接下来重启redis：

#首先查询到redis的pid后，kill掉,然后重启
[root@localhost bin]# ps -ef|grep redis
root      20940      1  0 12:12 ?        00:00:18 ./redis-server *:6379 
[root@localhost bin]# kill 20940
[root@localhost bin]# ./redis-server redis.conf 

1
2
3
4
5
6
后台启动成功如下


最后我们使用redis客户端通过密码远程连接：

#远程连接
./redis-cli -h 你服务器的ip -p 6379 -a 你的密码
1
2

————————————————
版权声明：本文为CSDN博主「linlangleo」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_35992900/article/details/82950157