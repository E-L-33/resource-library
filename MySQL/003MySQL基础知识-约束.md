#MySQL基础知识-约束


##约束
**约束是一种限制，它通过对表的行或列的数据做出限制，来确保表的数据的完整性、唯一性。**

创建表的万能模板：

	CREATE TABLE 表名(
    	字段名1 类型[(宽度) 列级别约束条件 默认值],
    	字段名2 类型[(宽度) 列级别约束条件 默认值],
    	字段名3 类型[(宽度) 列级别约束条件 默认值],
        。。。
        表级别约束条件
	);

### 一、约束分类
在MySQL中，通常有这几种约束：

|约束类型：|主键|默认值|唯一|外键|非空|
|-|-|-|-|-|
|关键字：|PRIMARY KEY|DEFAULT|UNIQUE|FOREIGN KEY|NOT NULL|

####建立含约束的表
#####1、主健约束
**主键 (PRIMARY KEY)**是用于约束表中的一行，作为这一行的唯一标识符，在一张表中通过主键就能准确定位到一行，因此主键十分重要。主键不能有重复且不能为空。

* 定义主键常见的有两种方式

	1)、在列级别约束条件里直接定义
		mysql>CREATE TABLE employee
          ->(
          ->id int(10) PRIMARY KEY,
          ->name char(11)
          ->);
        Query OK, 0 rows affected (0.09 sec)
	即执行成功，影响了0行数据
	&nbsp;
	2)、在表级别约束条件里定义
		mysql>CREATE TABLE employee
          ->(
          ->id int(10),
          ->name char(11)，
          ->PRIMARY KEY(id)
          ->);
        Query OK, 0 rows affected (0.09 sec)

* 还有一种特殊的主键——**复合主键**。主键不仅可以是表中的一列，也可以由表中的两列或多列来共同标识
		mysql>CREATE TABLE employee
          ->(
          ->id int(10),
          ->name char(11)，
          ->age int(4),
          ->PRIMARY KEY(id,name)
          ->);
        Query OK, 0 rows affected (0.09 sec)

&nbsp;

#####2、默认值约束
**默认值约束 (DEFAULT) **规定，当有 DEFAULT 约束的列，插入数据为空时，将使用默认值。
默认值约束语法规则：
&emsp;&emsp;**字段名　数据类型　DEFAULT 默认值**

	mysql>CREATE TABLE employee
        ->(
        ->id int(10),
        ->name char(11)，
        ->age int(4) DEFAULT 20,
        ->PRIMARY KEY(id,name)
        ->);
    Query OK, 0 rows affected (0.09 sec)

#####3、唯一约束
**唯一约束 (UNIQUE) **比较简单，它规定一张表中指定的一列的值必须不能有重复值，即这一列每个值都是唯一的。
当 INSERT 语句新插入的数据和已有数据重复的时候，如果有 UNIQUE约束，则 INSERT 失败，
唯一约束语法规则：
&emsp;&emsp;**字段名　数据类型　UNIQUE**

	mysql>CREATE TABLE employee
        ->(
        ->id int(10),
        ->name char(11) UNIQUE，
        ->age int(4) ,
        ->PRIMARY KEY(id,name)
        ->);
    Query OK, 0 rows affected (0.09 sec)
#####4、外键约束
**外键 (FOREIGN KEY)**既能确保数据完整性，也能表现表之间的关系。
一个表可以有多个外键，每个外键必须**REFERENCES (参考)**另一个表的主键，被外键约束的列，取值必须在它参考的列中有对应值。
定义外键语法规则：
&emsp;&emsp;**[CONSTRAINT <外键名>] FOREIGN KEY 字段名1[,字段名2,...]  REFERENCES <主表名>  主键列1[,主键列2,...]**
主表：

	mysql>CREATE TABLE student
        ->(
        ->id int(12) PRIMARY KEY,
        ->name varchar(10) NOT NULL,
        ->age int(6) NOT NULL,
        ->);
子表：

	mysql>CREATE TABLE grade
        ->(
        ->id int(12),
        ->subject varchar(10),
        ->score int(6),
        ->PRIMARY KEY(id,subject),
        ->FORIEGN KEY（id）REFERENCES student(id)
        ->);
**外键的补充说明：**

* 外键名可为空
* 外键用来在两个表的数据之间建立连接，它可以是一个列或者多个列。
* 一个表可以有一个或者多个外键。
* 外键对应的是参照完整性，一个表的外键可以为空值，若不为空值，则每一个外键值必须等于另一个表中主键的某个值（子表的外键必须关联父表的主键）
* 定义外键后，不允许删除在另一个表中具有关联关系的行。
* 主表(父表): 对于两个具有关联关系的表而言，相关联字段中主键所在的那个表即是主表。
* 从表(子表): 对于两个具有关联关系的表而言，相关联字段中外键所在的那个表即是从表。

#####5、非空约束
**非空约束 (NOT NULL)**,听名字就能理解，被非空约束的列，在插入值时必须非空。
非空约束语法规则：
&emsp;&emsp;**字段名　数据类型　NOT NULL**

	mysql>CREATE TABLE employee
        ->(
        ->id int(10),
        ->name char(11) NOT NULL，
        ->age int(4) NOT NULL,
        ->PRIMARY KEY(id,name)
        ->);
    Query OK, 0 rows affected (0.09 sec)


