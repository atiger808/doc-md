## [微信小程序使用npm安装第三方包](https://www.cnblogs.com/cokolxvd/p/11535134.html)

官方文档写的教程不够详细，根据查找到的成功方法重新整理出一个完整步骤

案例是安装Vant Weapp 一个小程序的UI库,参考网址([https://youzan.github.io/vant-weapp/](https://youzan.github.io/vant-weapp/))

首先使用npm当然要安装node.js，下面开始正式步骤。

1.控制台进入到小程序的目录

2.进行项目的初始化,成功之后便会在小程序目录先生成package.josn文件

```
1 npm init -f
```

-f表示force的意思，就是初始化全部按照默认值，不加-f则需要填写一些项目信息，因为只是做个试验就加-f 省事。

执行结果：

![img](https://img2018.cnblogs.com/blog/1531896/201909/1531896-20190917162739107-1225456718.png)

3.安装第三方依赖，这里是安装Vant Weapp

```
1 npm i vant-weapp -S --production
```

执行结果：

![img](https://img2018.cnblogs.com/blog/1531896/201909/1531896-20190917163121595-335392481.png)

 

 

 执行完成后会在小程序目录下新建一个node_modules，会将vant-weapp的文件存放在这个文件夹下

4.在微信开发者工具中勾选使用npm模块

![img](https://img2018.cnblogs.com/blog/1531896/201909/1531896-20190917163547548-1718568333.png)

5.构建npm，在微信开发者工具中工具选项中点击构建npm

![img](https://img2018.cnblogs.com/blog/1531896/201909/1531896-20190917163745794-1142543018.png)

![img](https://img2018.cnblogs.com/blog/1531896/201909/1531896-20190917163852934-73201422.png)

 

 ![img](https://img2018.cnblogs.com/blog/1531896/201909/1531896-20190917163902837-1519859058.png)

 

 构建完成之后小程序目录会多出一个下图的文件夹，然后就可以直接引用里面组件了

![img](https://img2018.cnblogs.com/blog/1531896/201909/1531896-20190917163929476-1519226.png)

 2019-12-28更新:

若在小程序的云函数中使用npm，无需进行初始化，但是需要先安装依赖

```
npm install --production
```

上传的时候选择

![img](https://img2018.cnblogs.com/blog/1531896/201910/1531896-20191028164649889-849737424.png)