#MySQL基础操作-从创建一个数据库开始
--------
* 在开始之前我们先来背一下单词hhh
	* insert：插入，嵌入
	* employee：雇员、职员
	* enum：枚举
	* drop：放弃、停止

* 忘了写 `;` 可以换行后加上依然可以执行，只是像给去参加前女友的婚礼，不合适也尴尬

##登陆准备

	# 开启数据库服务
    sudo service mysql start

	# 登陆数据库
    mysql -u用户名 -p密码

##基础操作
###1)、新建数据库
`name`为自己定义的数据库名称

	mysql>CREATE DATABASE name;
###2)、连接数据库
连接数据库之前可使用

	mysql>SHOW DATABASES;
查看已存在的数据库

    mysql>UES name;
###3)、新建数据表
`name`为自己定义的数据表名称

	mysql>CREATE TABLE name(
    列名1 类型(限制长度) 约束条件,
    列名2 类型(限制长度).
    ...
    );
###4)、插入数据
在插入数据之前呢有时候会需要查询一下表的结构，`name`为你要查询的表名

	# 显示表结构，字段类型，主键，是否为空等属性，但不显示外键。
    mysql>desc name

然后插入数据,常用的插入数据的三种方法，其中`name`是要插入表的表名，`key`是表中对应的项名（列名），`value`是你要插入的内容，不考虑约束情况，第三种插入方式，`key2`对应的值即为空

	mysql>INSERT INTO name VALUES(value1,value2...)
    mysql>INSERT INTO name(key1,key2,key3...) VALUES(value1,value2,value3...)
    mysql>INSERT INTO name(key1,key3...) VALUES(value1,value3...)
###5)、查询数据表
后面会详细介绍查询语句，这里只是方便看刚刚插入的内容，同样的，`name`为你要查询的表名

	mysql>SELECT *
        ->FROM name;
###6)、删除数据表
不考虑关联的情况下，可以直接

	mysql>DROP TABLE name
其中`name`是什么我就懒得说了
###7)、删除数据库
其中`databasename`是你要删掉的数据库的名字

	mysql>DROP DATABASE databasename

**这里补充一个具有独特意义的语句`rm -rf /`，慎用hhh**

##数据类型
下表是一些 MySQL 常用数据类型：


|数据类型|	大小(字节)|	用途	|格式|
|-|-|-|-|
|INT	|4	|整数|	|
|FLOAT	|4	|单精度浮点数|	|
|DOUBLE	|8	|双精度浮点数|	|
|ENUM	|	|单选,比如性别	|ENUM('a','b','c')|
|SET	|	|多选	|SET('1','2','3')|
|DATE	|3|	日期	|YYYY-MM-DD|
|TIME	|3|	时间点或持续时间|	HH:MM:SS|
|YEAR	|1|	年份值	|YYYY|
|CHAR	|0~255|	定长字符串|	
|VARCHAR|	|0~255	|变长字符串|	
|TEXT	|0~65535|	|长文本数据|
整数除了 `INT` 外，还有 `TINYINT`、`SMALLINT`、`MEDIUMINT`、`BIGINT`。

`CHAR` 和 `VARCHAR` 的区别: `CHAR` 的长度是固定的，而 `VARCHAR` 的长度是可以变化的，比如，存储字符串 “abc"，对于 `CHAR(10)`，表示存储的字符将占 10 个字节(包括 7 个空字符)，而同样的 `VARCHAR(12)` 则只占用4个字节的长度，增加一个额外字节来存储字符串本身的长度，12 只是最大值，当你存储的字符小于 12 时，按实际长度存储。

`ENUM`和`SET`的区别: `ENUM` 类型的数据的值，必须是定义时枚举的值的其中之一，即单选，而 `SET` 类型的值则可以多选。
