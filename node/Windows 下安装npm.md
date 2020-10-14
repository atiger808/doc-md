# [Windows 下安装NPM](https://www.cnblogs.com/interdrp/p/6779973.html)

### 第一步: 下载node.js的windows版

###  当前最新版本是https://nodejs.org/dist/

 

### 第二步:设置环境变量

把node.exe所在目录加入到PATH环境变量中。

配置成功后可以在CMD中通过node --version 看到node.js对应的版本号

C:\Users\fn>node --version
v6.10.2

### 第三步: 安装git

直接到以下地址 [https://git-scm.com/download/win ](https://git-scm.com/download/win%20)下载[Git](http://lib.csdn.net/base/git) windows安装文，按照提示一步步安装即可。

安装完成后把git安装bin目录加入PATH环境变量

找到git安装路径中bin的位置，如：D:\Program Files\Git\bin

找到git安装路径中git-core的位置，如：D:\Program Files\Git\libexec\git-core;

CMD中运行 `git --version` 确认安装是否成功

C:\Users\fn>git --version
git version 1.7.7.msysgit.1

### 第四步: 安装 npm

在确保node.exe和git都在PATH环境变量中后执行以下命令:

```
git config --system http.sslcainfo /bin/curl-ca-bundle.crt
```

```
git clone --recursive git://github.com/isaacs/npm.git


```

 

```
cd npm
```

```
node cli.js install npm -gf
```

下面来测试一下是否成功，一切OK开始Node.JS之旅

D:\develop\nodejs\hello>npm install -d
npm info it worked if it ends with ok
npm info using npm@1.0.103
npm info using node@v0.5.10
npm info preinstall application-name@0.0.1
npm info addNamed [ 'jade', '>= 0.0.1' ]
npm info addNamed [ 'express', '2.5.0' ]

最好设置下国内镜像要不然下载会很慢

github npm 撞墙的解决方案。 
github： 
代理服务器是必须的，我用的是本地的astrill 
给curl设置代理 
export http_proxy="127.0.0.1:3213" 
export https_proxy="127.0.0.1:3213" 
ok了 