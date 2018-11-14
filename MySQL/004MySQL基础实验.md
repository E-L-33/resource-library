搭建一个简易的成绩管理系统的数据库
介绍
现需要构建一个简易的成绩管理系统的数据库，来记录几门课程的学生成绩。数据库中有三张表分别用于记录学生信息、课程信息和成绩信息。

数据库表的数据如下：

学生表(student)：学生 id 、学生姓名和性别

此处输入图片的描述

课程表：课程 id 和课程名

此处输入图片的描述

成绩表：成绩 id 、学生 id 、课程 id 和分数

此处输入图片的描述

服务器中的 MySQL 还没有启动，请注意 MySQL 的 root 账户默认密码为空。

目标
1.MySQL 服务处于运行状态

2.新建数据库的名称为 gradesystem

3.gradesystem 包含三个表：student、course、mark；

student 表包含3列：sid(主键)、sname、gender；
course 表包含2列：cid(主键)、cname；
mark 表包含4列：mid(主键)、sid、cid、score ，注意与其他两个表主键之间的关系。
4.将上述表中的数据分别插入到各个表中

提示
建立表时注意 id 自增和键约束
每个表插入语句可通过一条语句完成



mysql> CREATE TABLE student ( sid int(12) PRIMARY KEY, sname varchar(10), gender enum('male','female') );

mysql> CREATE TABLE course ( cid int(12) PRIMARY KEY, cname varchar(10) );

	CREATE TABLE mark 
	( 
	mid int(12) PRIMARY KEY, 
	sid int(12), 
	cid int(12), 
	score int(10), 
	FOREIGN KEY(sid) REFERENCES student(sid), 
	FOREIGN KEY(cid) REFERENCES course(cid) 
	);

