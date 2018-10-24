##SQL学习准备-安装与配置
###一、 安装前检查

输入命令尝试打开MySQL服务，可判断是否有安装：

    # sudo service mysql start

如果出现

	* Starting MySQL database server mysqld                                 [ OK ] 
表示已经安装了，没有则需要重新安装

###二、 CentOS 7下安装配置MySQL
虽然[实验楼](https://www.shiyanlou.com/courses/9)的课程教授和用到的是Ubuntu，但是我安装使用的是CentOS，这里也就当作是顺带补充一下CentOS下的MySQL安装与配置:
####一般安装方式为：

	# yum install mysql
	# yum install mysql-server
	# yum install mysql-devel

安装mysql和mysql-devel都成功，但是安装mysql-server失败，如下：

	[root@yl-web yl]# yum install mysql-server
	Loaded plugins: fastestmirror
	Loading mirror speeds from cached hostfile
	 * base: mirrors.sina.cn
	 * extras: mirrors.sina.cn
	 * updates: mirrors.sina.cn
	No package mysql-server available.
	Error: Nothing to do
参考资料发现是CentOS 7 版本将MySQL数据库软件从默认的程序列表中移除，用mariadb代替了。

有两种解决办法：

1. 方法一：安装mariadb（此处不做介绍，有需要的可参考文后的参考文章）
2. 方法二：官网下载安装mysql-server


    # wget http://dev.mysql.com/get/mysql-community-release-el7-5.noarch.rpm
	# rpm -ivh mysql-community-release-el7-5.noarch.rpm
	# yum install mysql-community-server

安装成功后重启mysql服务：

	# service mysqld restart

初次安装后设置密码：

	# mysql -u root
	mysql> set password for 'root'@'localhost' =password('password');
	Query OK, 0 rows affected (0.00 sec)
	mysql> 

####配置mysql(选做)

#####1、 编码
mysql配置文件为/etc/my.cnf
最后加上编码配置

	[mysql]
	default-character-set =utf8
这里的字符编码必须和/usr/share/mysql/charsets/Index.xml中一致。


#####2、 远程连接设置

把在所有数据库的所有表的所有权限赋值给位于所有IP地址的root用户。

	mysql> grant all privileges on *.* to root@'%'identified by 'password';

如果是新用户而不是root，则要先新建用户

	mysql>create user 'username'@'%' identified by 'password';

###三、初步使用
#####1、 打开数据库

	# 启动 MySQL 服务
	sudo service mysql start

	# 使用 root 用户登录
	mysql -u帐号 -p密码

    # 实验楼由于没有密码所以可以直接登陆
    mysql -u root

#####2、 查看数据库

	mysql>show databases;
    # 写惯了Python 的千万别忘了句尾的 ';'

#####3、 连接数据库

	mysql>use databasename;

#####4、 查看表

	mysql>show tables;

#####5、 退出

    # 三种办法都可以的
	mysql > exit;
	mysql > quit;
	mysql > \q;

以上    


-------------------------------------
参考资料：[1]、[centos7 mysql数据库安装和配置](https://www.jb51.net/article/103118.htm)