1. # 树莓派安装MariaDB，使用MariaDB替代mysql

   # 在树莓派上配置MariaDB

   ## 前言

   MariaDB是由原本开发MySQL的一些原始开发者领导，他们担心Oracle收购MySQL后会有一些隐患。MariaDB与MySQL保持这高度兼容性，并使用了一个新的存储引擎Aria。

   ## 安装MriaDB

   ```
   sudo apt-get install mariadb-server 
   ```

   静静的等待安装完成即可，中间会询问是否继续，输入Y继续即可。安装完成后就可以通过一下命令连接到MariaDB

   ```
   sudo mysql 
   ```

   出现如下讯息表示已成功连接到MariaDB了

   ```
   Welcome to the MariaDB monitor. Commands end with ; or \g. 

   MariaDB [(none)]> 
   ```

   ## 配置密码访问

   默认情况下MariaDB安装好后都没有配置访问用户的密码，因此如果需要远程连接时会无法连接。因此需要先對root用户设置密码。首先透过上一步中的命令连接至MariaDB，输入如下语句进行密码的修改

   ```
   use mysql; 
   update user set plugin='mysql_native_password';  #重置加密方式
   update user set password=PASSWORD("newpassword") where User='root';  #设置新密码
   flush privileges; 
   ```

   以上执行完成后，重启服务

   ```
   sudo systemctl restart mariadb 
   ```

   重启完成后，试用密码进行mariadb登录，验证是否修改成功

   ```
   mysql -u root -p 
   ```

   输入上面设置的密码就可以看到第一步安装完成登录时一样的画面了。

   ## 配置MariaDB可远程连接

   MariaDB默认只监听了127.0.0.1这个IP地址，这个时候是无法从外部连接到树莓派上MariaDB。
   先使用一下命令打开配置文件

   ```
   nano /etc/mysql/mariadb.conf.d/50-server.cnf
   ```

   打开文件后有一段如下的内容:

   ```
   # Instead of skip-networking the default is now to listen only on



   # localhost which is more compatible and is not less secure.



   # bind-address            = 127.0.0.1
   ```

   bind-address表示只监听了127.0.0.1这个IP，将这一行的前面加上# 将这一行注释起来，这样MariaDB就监听了所有的IP。
   此时从外部的电脑连接MariaDB会提示"xxx.xxx.xxx is not allowed to connect to this MariaDB Server"。同样使用上一步中的mysql命令连接到MariaDB，输入如下命令：

   ```
   GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'password' WITH GRANT OPTION;



   --格式如下



   GRANT ALL PRIVILEGES ON *.* TO 'user'@'remoteip' IDENTIFIED BY 'password' WITH GRANT OPTION;



   --更新权限



   FLUSH PRIVILEGES;
   ```

   至此可从外部连接到树莓派上的MariaDB了



# 如何跳过验证登录mysql

修改/etc/mysql/mariadb.conf.d下文件 50-server.cnf

在[mysqld] 后添加 skip-grant-tables

```
# These groups are read by MariaDB server.
# Use it for options that only the server (but not clients) should see
#
# See the examples of server my.cnf files in /usr/share/mysql

# this is read by the standalone daemon and embedded servers
[server]

# this is only for the mysqld standalone daemon
[mysqld]
skip-grant-tables

#
# * Basic Settings
#
user                    = mysql
pid-file                = /run/mysqld/mysqld.pid
socket                  = /run/mysqld/mysqld.sock
#port                   = 3306
basedir                 = /usr
datadir                 = /var/lib/mysql
tmpdir                  = /tmp
lc-messages-dir         = /usr/share/mysql
#skip-external-locking

```







# 树莓派中卸载MySQL

羞羞的铁拳_$ 2019-05-04 11:35:41  670  收藏 2
展开

##### 1、停止服务：sudo service mysql stop

##### 2、卸载MySQL：

     （1）sudo apt-get --purge remove mysql-server
     （2）sudo apt-get --purge remove mysql-client
     （3）sudo apt-get --purge remove mysql-common

##### 3、清理残余

    （1）sudo apt-get autoremove
    （2）sudo apt-get autoclean
   （3）rm /etc/mysql/ -R
    （4）rm /var/lib/mysql/ -R
