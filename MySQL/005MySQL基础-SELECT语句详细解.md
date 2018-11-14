#MySQL基础-SELECT语句详解
-----------------
包含以下内容:

* SELECT 基本语法
* 数学符号条件
* AND/OR与IN/NOT IN
* 通配符
* 排序
* 分组
* SQL 内置函数和计算
* 子查询与连接查询

文中使用的数据库或者表可以在文末环境准备复制，

##SELECT语句介绍
SELECT 语句的基本格式为：
&emsp;&emsp;**SELECT 要查询的列名 FROM 表名字 WHERE 限制条件;**
我们之前用到的 `SELECT * FROM name` 中的`*`表示查询表中的所有的列

SELECT 语句常常会有 WHERE 限制条件，用于达到更加精确的查询。WHERE限制条件可以有数学符号(`=,<,>,>=,<=`)

	mysql>SELECT name,age FROM employee WHERE age>25;
筛选出 age 大于 25 的结果：
或者查找一个名字为 Mary 的员工的 name,age 和 phone：

	mysql>SELECT name,age,phone FROM employee WHERE name='Mary';

##数学符号条件
SELECT 语句常常会有 WHERE 限制条件，用于达到更加精确的查询。WHERE限制条件可以有数学符号 (=,<,>,>=,<=) ，刚才我们查询了 name 和 age，现在稍作修改：

	mysql>SELECT name,age FROM employee WHERE age>25;
筛选出 age 大于 25 的结果：

##AND/OR与IN/NOT IN
WHERE 后面可以有不止一条限制，而根据条件之间的逻辑关系，可以用 **OR(或)** 和 **AND(且)** 连接：

    #筛选出 age 小于 25，或 age 大于 30
	mysql>SELECT name,age FROM employee WHERE age<25 OR age>30;

    #筛选出 age 大于 25，且 age 小于 30
	mysql>SELECT name,age FROM employee WHERE age>25 AND age<30;

而刚才的限制条件 `age>25 AND age<30`，如果需要包含25和30这两个数字的话，可以替换为 `age BETWEEN 25 AND 30`

    #筛选出 age 小 于 等 于 30 且 age 大 于 等 于25
	mysql>SELECT name,age FROM employee WHERE age BETWEEN 25 AND 30;

关键词**IN**和**NOT IN**的作用和它们的名字一样明显，用于筛选“在”或“不在”某个范围内的结果，比如说我们要查询在dpt3或dpt4的人:

	mysql>SELECT name,age,phone,in_dpt FROM employee WHERE in_dpt IN ('dpt3','dpt4');

而NOT IN的效果则是，如下面这条命令，查询出了不在dpt1也不在dpt3的人：

	mysql>SELECT name,age,phone,in_dpt FROM employee WHERE in_dpt NOT IN ('dpt1','dpt3');

##通配符
关键字 `LIKE` 在SQL语句中和通配符一起使用，通配符代表未知字符。SQL中的通配符是 `_` 和 `%` 。其中 `_` 代表**一个**未指定字符，`%` 代表**不定个**未指定字符。

比如，要只记得电话号码前四位数为1101，而后两位忘记了，则可以用两个 `_` 通配符代替：

	mysql>SELECT name,age,phone FROM employee WHERE phone LIKE '1101__';

这样就查找出了1101开头的6位数电话号码：

另一种情况，比如只记名字的首字母，又不知道名字长度，则用 `%` 通配符代替不定个字符：

	mysql>SELECT name,age,phone FROM employee WHERE name LIKE 'J%';

这样就查找出了首字母为 J 的人

##排序
为了使查询结果看起来更顺眼，我们可能需要对结果按某一列来排序，这就要用到 `ORDER BY`排序关键词。默认情况下，`ORDER BY`的结果是升序排列，而使用关键词`ASC`和`DESC`可指定升序或降序排序。 比如，我们按salary降序排列，SQL语句为：

	mysql>SELECT name,age,salary,phone FROM employee ORDER BY salary DESC;

##分组
有时需要将结果按照分类汇总，`GROUP BY`就是用来处理的函数，比如查询今年25岁的有多少人：

	mysql>SELECT in_dpt,COUNT(id) FROM employee GROUP BY(in_dpt);

简单来讲，`GROUP BY`就是对数据表按要查询的列分组，然后对组里面的人进行`COUNT`，也就是说，这里虽然是`COUNT(id)`，但是在这里COUNT的作用只是对某一列进行计数，所以这里不论是`COUNT(age)`、`COUNT(name)`还是`COUNT(salary)`得到的结果都是一样的，没有区别
当然，也可以对分组进行其他计算，比如，求部门dpt1里面人的平均年龄：

	mysql>SELECT in_dep,AVG(age) AS avg_age FROM employee GROUP BY(in_dpy);

	# 并且找出最高年纪
    mysql>SELECT in_dep,AVG(age) AS avg_age，MAX(age) FROM employee GROUP BY(in_dpy);

更详细的分组说明见[SQL语句汇总（三）——聚合函数、分组、子查询及组合查询](https://www.cnblogs.com/ghost-xyx/p/3811036.html)

##SQL 内置函数和计算（聚合函数）
前面我们用到了`COUNT`和`AVG`对数据进行处理，用到的就是SQL里的内置函数
SQL 允许对表中的数据进行计算。对此，SQL 有 5 个内置函数，这些函数都对 SELECT 的结果做操作：

|函数名：|COUNT|	SUM|	AVG|	MAX|	MIN|
|-|-|-|-|-|-|
|作用:|计数|	求和|	求平均值|	最大值	|最小值|

> 其中 COUNT 函数可用于任何数据类型(因为它只是计数)，而 SUM 、AVG 函数都只能对数字类数据类型做计算，MAX 和 MIN 可用于数值、字符串或是日期时间数据类型。

具体举例，比如计算出salary的最大、最小值，用这样的一条语句：

	mysql>SELECT MAX(salary) AS max_salary,MIN(salary) FROM employee;

有一个细节你或许注意到了，使用**`AS`关键词可以给值重命名**，比如最大值被命名为了max_salary：


##子查询与连接查询


##环境准备
搭建好一个名为mysql_shiyan 的数据库(有三张表：department，employee，project)，并向其中插入数据。

	CREATE DATABASE mysql_shiyan;

	use mysql_shiyan;

	CREATE TABLE department
	(
	  dpt_name   CHAR(20) NOT NULL,
	  people_num INT(10) DEFAULT '10',
	  CONSTRAINT dpt_pk PRIMARY KEY (dpt_name)
	 );

	CREATE TABLE employee
	(
	  id      INT(10) PRIMARY KEY,
	  name    CHAR(20),
	  age     INT(10),
	  salary  INT(10) NOT NULL,
	  phone   INT(12) NOT NULL,
	  in_dpt  CHAR(20) NOT NULL,
	  UNIQUE  (phone),
	  CONSTRAINT emp_fk FOREIGN KEY (in_dpt) REFERENCES department(dpt_name)
	);

	CREATE TABLE project
	(
	  proj_num   INT(10) NOT NULL,
	  proj_name  CHAR(20) NOT NULL,
	  start_date DATE NOT NULL,
	  end_date   DATE DEFAULT '2015-04-01',
	  of_dpt     CHAR(20) REFERENCES department(dpt_name),
	  CONSTRAINT proj_pk PRIMARY KEY (proj_num,proj_name)
	 );

---------
向表中插入数据
	#INSERT INTO department(dpt_name,people_num) VALUES('部门',人数);

	INSERT INTO department(dpt_name,people_num) VALUES('dpt1',11);
	INSERT INTO department(dpt_name,people_num) VALUES('dpt2',12);
	INSERT INTO department(dpt_name,people_num) VALUES('dpt3',10);
	INSERT INTO department(dpt_name,people_num) VALUES('dpt4',15);


	#INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(编号,'名字',年龄,工资,电话,'部门');

	INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(01,'Tom',26,2500,119119,'dpt4');
	INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(02,'Jack',24,2500,120120,'dpt2');
	INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(03,'Rose',22,2800,114114,'dpt3');
	INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(04,'Jim',35,3000,100861,'dpt1');
	INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(05,'Mary',21,3000,100101,'dpt2');
	INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(06,'Alex',26,3000,123456,'dpt1');
	INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(07,'Ken',27,3500,654321,'dpt1');
	INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(08,'Rick',24,3500,987654,'dpt3');
	INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(09,'Joe',31,3600,110129,'dpt2');
	INSERT INTO employee(id,name,age,salary,phone,in_dpt) VALUES(10,'Mike',23,3400,110110,'dpt4');
	INSERT INTO employee(id,name,salary,phone,in_dpt) VALUES(11,'Jobs',3600,019283,'dpt2');
	INSERT INTO employee(id,name,salary,phone,in_dpt) VALUES(12,'Tony',3400,102938,'dpt3');

	#INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(编号,'工程名','开始时间','结束时间','部门名');

	INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(01,'proj_a','2015-01-15','2015-01-31','dpt2');
	INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(02,'proj_b','2015-01-15','2015-02-15','dpt1');
	INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(03,'proj_c','2015-02-01','2015-03-01','dpt4');
	INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(04,'proj_d','2015-02-15','2015-04-01','dpt3');
	INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(05,'proj_e','2015-02-25','2015-03-01','dpt4');
	INSERT INTO project(proj_num,proj_name,start_date,end_date,of_dpt) VALUES(06,'proj_f','2015-02-26','2015-03-01','dpt2');
