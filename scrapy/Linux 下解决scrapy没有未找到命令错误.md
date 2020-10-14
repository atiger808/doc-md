## [Linux 下解决scrapy没有未找到命令错误](https://www.cnblogs.com/wtil/p/11853465.html)

系统：deepin

错误提示：

pip3 安装scrapy之后，提示：bash: scrapy: 未找到命令

解决方法：

1. 进入root权限
2. 创建软连接
   1. ln -s /home/用户名/.local/bin/scrapy /usr/bin/scrapy
   2. 解决完毕