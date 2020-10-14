（二）PhantomJS下载

1）使用**wget**命令下载：

> `wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2`

2）解压并且创建软链接

```
tar -xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2 
sudo cp -R phantomjs-2.1.1-linux-x86_64 /usr/local/share/ 
sudo ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/

```

（三）Selenium的安装

> 直接使用Pip3 命令：
> `pip3 install selenium`

## 验证selenium与phantomjs是否成功安装

1）Linux 下创建一个新文件命名为test.py里面写入以下代码：

```
from selenium import webdriver

driver = webdriver.PhantomJS()    
driver.get('http://www.baidu.com/')
print driver.page_source
```