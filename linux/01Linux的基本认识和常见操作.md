# Linux的基本认识和常见操作

#### 1.基本认知

#### 2.常见操作

#### 3.卸载软件



### 1.基本认知

**1.Linux由来**

```
Linux操作系统是基于UNIX操作系统的， 其内核主要是由C程序编写。Linux是自由和开放的，任何组织和个人只要遵循GNU通用公共许可证协议都可以自由免费地使用Linux的所有底层源代码，并可以自由地修改和分发。
```

**2.Linux的目录结构**

```
Linux和Windows最大的不同之处在于Linux的目录结构的设计，在Linux中，任何文件，目录和设备都在根目录“/”之下。Linux把所有文件和设备都当作文件来管理，这些文件都在根目录下，同时Linux中的文件名区分大小写。
```

![Linux目录结构](C:\Users\不动\Desktop\python进阶\1Linux\Linux目录结构.png)

**3.命令提示符**

`[root@budong ~]#`

格式：`[用户@主机名 当前目录]#`

`root `是`Linux`管理员，也称为超级用户

这里的`budong `是主机名

`~`是当前用户的家目录，家目录就相当于我们`window`系统中的桌面。

`#`是超级用户的提示符，`$`是普通用户的提示符。

命令：`pwd`  当前目录  、`hostname` 主机名、`whoami`  当前用户

```shell
[root@budong ~]# pwd
/root
[root@budong ~]# hostname
budong
[root@budong ~]# whoami
root
```

**4.Linux的用户**

在Linux中`root`用户具有超级权限，可以操作任何文件，日常使用中应该避免使用它。这就需要我们在平常使用的过程中使用普通用户。

在Linux中有三种用户，超级用户、系统用户和普通用户，超级用户就是root用户；系统用户是系统正常使用时使用的账户，如bin、mail等，但是系统用户不能够登录；普通用户是普通使用者，能够使用Linux大部分资源，但是一些特定的权限受到控制。

在Linux中可以使用`cat /etc/passwd`查看当前的用户

```shell
root:x:0:0:root:/root:/bin/bash
#用户名称:用户密码：用户标记号：组标记号：相关注释：主目录：使用的Shell
#root用户可以使用 cat /etc/shadow 查看加密后的用户密码
```

**5.Linux的用户管理**

​	**1.添加用户**

```shell
[root@budong ~]# useradd budong
[root@budong ~]# passwd budong
更改用户 budong 的密码 。
新的 密码：
无效的密码： 它基于字典单词
无效的密码： 过于简单
重新输入新的 密码：
passwd： 所有的身份验证令牌已经成功更新。
[root@budong ~]# 
##在添加用户之后，给用户改密码
```

​	**2.为普通用户添加sudo权限**

```shell
[root@budong ~]# visudo
#在root ALL=(ALL)       ALL  #这行下面添加如下
budong  ALL=(ALL)       ALL
```

`visudo` 打开文件后，将`username ALL=(ALL)  ALL `加入到文件中。具体步骤：

​	1.visudo进入文件。

​	2.按上下键找到`root    ALL=(ALL)       ALL` 这一行内容。

​	3.按 i 键进入插入模式，然后输入`username ALL=(ALL)  ALL ` 。

​	4.输入完成后，按Esc，然后shift+;   ,末行出现冒号后输入wq回车来保存退出。

在完成上面的步骤之后我们就可以使用普通用户登陆，xshell这里也是，可以是用普通用户，不用担心root权限过大造成关系文件的误操作。



### 2.常见操作

**1.目录跳转`cd`**

语法：`cd (选项) (参数)`

常见用法：

```
cd 绝对路径
cd 相对路径
cd .. 回到上一级目录
cd / 跳到根目录
cd ~ 回到家目录
cd   回到家目录
cd . 当前目录
cd - 回到上一次目录
```

查看目录内容的命令配合着cd命令一起学习

```
ls 查看当前目录中的内容
ll 详细列出当前目录中的内容
```

目录结构：

```
~家目录
/根目录  从逻辑上说系统中的所有一切都隶属于它
/bin		--存放所有用户都能执行的命令（二制文件）
/boot		--存放启动文件/内核的相关文件，一般独立成为一个分区。
/dev		--存放物理设备的目录
/etc		--存放配置文件
/home		--用户的家目录
/lib		--32位库文件
/lost+found	--分区修复时找回来的文件会存放在这里,
              存放一些系统不正常关机的的文件残片
/media		--专门用于挂载的目录
/misc		--autofs备用文件夹
/mnt		--专门用于挂载的目录
/opt		--用于存放第三方软件可选目录
/proc		--当前内核的映射，一个虚拟的文件系统
/root		--管理root的家目录
/sbin		--管理员才能够执行的命令  root
/selinux	--selinux安全策略相关的文件
/sys		--内核在内存中的映像文件
/tmp		--临时目录，建议独立划成分区
/usr		--用于存放第三方软件
/var		--存放日志或者频繁修改的文件
```



**2.查看目录下的文件`ls`**

语法：`ls（选项）（参数）`

选项

```
-a：显示所有档案及目录（ls内定将档案名或目录名称为“.”的视为影藏，不会列出）
-C：多列显示输出结果。这是默认选项；
-l：与“-C”选项功能相反，所有输出信息用单列格式输出，不输出为多列；
-F：在每个输出项后追加文件的类型标识符，具体含义：“*”表示具有可执行权限的普通文件，“/”表示目录，“@”表示符号链接，“|”表示命令管道FIFO，“=”表示sockets套接字。当文件为普通文件时，不输出任何标识符；
-b：将文件中的不可输出的字符以反斜线“”加字符编码的方式输出；
-c：与“-lt”选项连用时，按照文件状态时间排序输出目录内容，排序的依据是文件的索引节点中的ctime字段。与“-l”选项连用时，则排序的一句是文件的状态改变时间；
-d：仅显示目录名，而不显示目录下的内容列表。显示符号链接文件本身，而不显示其所指向的目录列表；
-f：此参数的效果和同时指定“aU”参数相同，并关闭“lst”参数的效果；
-i：显示文件索引节点号（inode）。一个索引节点代表一个文件；
--file-type：与“-F”选项的功能相同，但是不显示“*”；
-k：以KB（千字节）为单位显示文件大小；
-l：以长格式显示目录下的内容列表。输出的信息从左到右依次包括文件名，文件类型、权限模式、硬连接数、所有者、组、文件大小和文件的最后修改时间等；
-m：用“,”号区隔每个文件和目录的名称；
-n：以用户识别码和群组识别码替代其名称；
-r：以文件名反序排列并输出目录内容列表；
-s：显示文件和目录的大小，以区块为单位；
-t：用文件和目录的更改时间排序；
-L：如果遇到性质为符号链接的文件或目录，直接列出该链接所指向的原始文件或目录；
-R：递归处理，将指定目录下的所有文件及子目录一并处理；
```

常见用法

```shell
[root@budong ~]# ls
[root@budong ~]# ll
[root@budong ~]# ls -lrt  #最新更改的文件在最下面
[budong@budong /]$ ls -a
```



##### **3.创建/删除目录`mkdir` `rmdir`**

语法：`mkdir (选项)(参数)`    `rmdir(选项)(参数)`

```shell
[budong@budong ~]$ mkdir test  #创建文件夹 test
[budong@budong ~]$ ls
[budong@budong ~]$ cd test/  #进入文件夹
[budong@budong test]$ mkdir a  #创建文件夹  a
[budong@budong test]$ ls
[budong@budong test]$ mkdir b
[budong@budong test]$ rmdir b  #删除文件夹
[budong@budong test]$ ls
[budong@budong test]$ cd ..
[budong@budong ~]$ rmdir test
rmdir: 删除 "test" 失败: 目录非空   #test文件夹下有a文件夹，所以不能直接删除
```



**4.创建/删除文件`touch` `rm`**

语法：touch(选项)(参数)

touch命令有两个功能：一是用于把已存在文件的时间标签更新为系统当前的时间（默认方式），它们的数据将原封不动地保留下来；二是用来创建新的空文件

选项

```
-a：或--time=atime或--time=access或--time=use  只更改存取时间；
-c：或--no-create  不建立任何文件；
-d：<时间日期> 使用指定的日期时间，而非现在的时间；
-f：此参数将忽略不予处理，仅负责解决BSD版本touch指令的兼容性问题；
-m：或--time=mtime或--time=modify  只更该变动时间；
-r：<参考文件或目录>  把指定文件或目录的日期时间，统统设成和参考文件或目录的日期时间相同；
-t：<日期时间>  使用指定的日期时间，而非现在的时间；
```

文件类型:

```
b      块文件也叫设备文件也叫特殊文件
c      字符文件
d      目录文件
p      管道文件
f(-)   普通文件／文本文件
l      链接文件
s(socket)      unix/类unix套接字
```

注意：linux上文件的后缀名只是给我们自己看的，并不能表示文件的类型。

语法：`rm (选项)(参数)`

`rm` 删除文件或目录

选项

```
-d：直接把欲删除的目录的硬连接数据删除成0，删除该目录
-f：强制删除文件或目录
-i：删除已有文件或目录之前先询问用户
-r或-R：递归处理，将指定目录下的所有文件与子目录一并处理
```



```
rm -i 删除前提示用户进行确认
rm -r 删除指定目录及目录下的所有文件
rm -f 强制删除，没有提示确认
```



**5.复制/移动文件`cp` `mv`**

`cp` 复制文件或目录，默认情况下，cp命令不能复制目录，如果要复制目录，则必须使用-r选项；

`mv` 对文件/目录重命名或移动文件

`cat`获取文件内容

```shell
[budong@budong ~]$ mkdir test
[budong@budong ~]$ touch a.py

[budong@budong ~]$ cp a.py b.py
[budong@budong ~]$ ls
a.py  b.py  test

[budong@budong ~]$ cp a.py test/
[budong@budong ~]$ cd test/
[budong@budong test]$ ls
a.py

[budong@budong ~]$ cp a.py test/b.py
[budong@budong ~]$ cd test/
[budong@budong test]$ ls
a.py  b.py

[budong@budong ~]$ cp /etc/passwd test/

[budong@budong ~]$ mv a.py aa.py
[budong@budong ~]$ ls
aa.py  b.py  test
[budong@budong ~]$ mv aa.py test/
[budong@budong ~]$ mv test haha
[budong@budong ~]$ ls
b.py  haha
```



**6.查看帮助**

`help`   简单帮助

`command(out)  --help`  外部命令

`help command(build_in)`  内部命令

安装man命令: `sudo yum install man`

`man` 命令，查看帮助信息时和`less`命令 查看文档一样

```
less 命令使用技巧：
直接上下键到跳行
下一行： e
上一行： y
下一页： 空格键 或 f 或 z
上一页： b 或 w
/string ： 向下搜寻string这个字符串
？string : 向上搜寻string这个字符串
n,N  ：n 继续下一个搜寻，N进行反向搜寻
帮助信息：h
退出 ： q 
```

### 3：卸载软件的命令

```
方法一、如果你知道要删除软件的具体名称，可以使用

sudo apt-get remove --purge 软件名称  
sudo apt-get autoremove --purge 软件名称 
1
2
方法二、如果不知道要删除软件的具体名称，可以使用

dpkg --get-selections | grep ‘软件相关名称’
```



