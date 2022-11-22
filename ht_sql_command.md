# template

> [参考链接](http://t.csdn.cn/H7rD0)

- 创建数据库

```
create database ht_test1;
```

- 查询数据库：

```
show databases;#查看所有数据库
select database();#查看当前使用的库
show create database db1;# 查询创建的数据库的语法
```

- 修改数据库编码：

```
alter database 库名 charset 编码类型；
```

- 删除数据库：

```mysql
drop  database 库名；
```

- 指定当前使用的数据库：

```mysql
use 库名
```

```

```

- 

```
create table employer(id int(8),name char(20));
```

- 查看当前数据库下所有表：

```
show tables;
```

- 查看表的结构：

```mysql
DESC 表名;
```

- **修改表名：**

```mysql
alter table 表名 rename 新表名;
```

- **添加列**

```
alter table 表名 add 列名 数据类型 约束条件，add 列名 数据类型 约束条件...;#添加列到最后面：
alter table 表名 add 列名 数据类型 约束条件 first;#添加列到最前面
alter table 表名 add 列名 数据类型 约束条件 after  已有的列名;#添加列到任意位置

```

- **删除列**

```
alter table 表名 drop 列名;
```

- **修改列**

```
alter table 表名 modify 列名 新数据类型;#修改列的数据类型：
alter table 表名 change 旧列名 新列名 新数据类型 新约束；#修改列的列名和数据类型：
```

- **删除表**

```
drop table 表名;
```

- 

```
create database database_student;
use database_student;
CREATE Table Student (sno char(6) Primary Key,sname char(10),ssex char(2),sbirth Date,sdept varchar(20));
```

- 

```
CREATE Table Course (cno char(6) Primary Key,cname varchar(20), cpno char(6));


```

- 

```
CREATE Table SC (sno char(6),cno char(6),grade Dec(4,1),Primary Key(sno,cno),Foreign Key(sno) references student(sno),Foreign Key(cno) references course(cno));
```

- 

```
CREATE Table Student (
Sno char(6) Primary Key,
Sname char(10) Not Null,
Ssex char(2) Default '男',
Sbirth Date,
Sdept varchar(20),
Check (Ssex in ('男','女'))
);
```

- 

```
CREATE Table SC 
(sno char(6),
cno char(6),
grade Dec(4,1),
Primary Key(sno,cno),
Foreign Key(sno) references student(sno),
Foreign Key(cno) references course(cno),
Check (Grade Between 0 and 100)
);
```

- 

```
ALTER Table Student ADD Status char(20) NOT NULL;
```

- 

```
ALTER Table Student ADD UNIQUE(Sname);
ALTER Table Student ADD CONSTRAINT mx_unique UNIQUE(Sname);
```

- 

```
ALTER Table Student ALTER Column Status char(30);

ALTER Table Student MODIFY Column Status char(30);
```

- 

```
ALTER Table Student DROP Column Status;
```

- 

```
ALTER Table Student DROP CONSTRAINT mx_unique;
```

- 

```
DROP Table Student;
```

- 

```
SELECT * FROM Student;
SELECT count(*) FROM Student;
```

- 

```
SELECT Sno FROM SC;
SELECT DISTINCT Sno FROM SC;
SELECT count(DISTINCT Sno) FROM SC;
```

- 

```
SELECT Sno,Sname,year(Getdate())-year(Sbirth)+1 FROM Student;


```

- 

```
SELECT Sno as 学号,Sname as 姓名,year(Getdate())-year(Sbirth)+1 as 年龄 FROM Student;
SELECT Sno as 学号,Sname as 姓名,year(curdate())-year(Sbirth)+1 as 年龄 FROM Student; 

SELECT Sno as 学号,Sname as 姓名,year(curdate())-year(Sbirth)+1 as 年龄 FROM Student ORDER By Age;
SELECT Sno as 学号,Sname as 姓名,year(curdate())-year(Sbirth)+1 as 年龄 FROM Student ORDER By 3;
```

- 

```
SELECT * FROM SC Order By Cno,Grade DESC;
SELECT * FROM SC Order By 2,3 DESC;
```

- 

```
SELECT Sname,Sbirth FROM Student WHERE Sbirth BETWEEN '1999-01-01' AND '2002-01-01';
```

- 

```
SELECT Sname,Sbirth FROM Student WHERE Sbirth>='1999-01-01' AND Sbirth<='2002-01-01';
```

- 

```
SELECT Sno,Sname FROM Student WHERE Sname LIKE '刘%';
SELECT Sno,Sname FROM Student WHERE Sname LIKE '_君%';
```

- 

```
SELECT * FROM Course WHERE Cname LIKE '%\_实验';
```

- 

```
SELECT * FROM Student WHERE Sdept Not IN ('MA','CS');
```

- 

```
SELECT Sno,Cno FROM SC WHERE Grade IS NULL;
```

- 先WHERE 再 GROUP ，再HAVING，最后SELECT

```
SELECT Sno as 学号,AVG(Grade) as 平均成绩 FROM SC GROUP BY Sno;
SELECT Sno as 学号,AVG(Grade) as 平均成绩, SUM(Grade) as 总成绩 FROM SC GROUP BY Sno;
```

- 

```
SELECT Sno as 学号,AVG(Grade) as 平均成绩 FROM SC GROUP BY Sno HAVING AVG(Grade)>=90;
```

- HAVING 是对组筛选 WHERE是对一个元组进行筛选

```
SELECT Sno as 学号,AVG(Grade) as 平均成绩 FROM SC GROUP BY Sno HAVING AVG(Grade)>=90;
```

- 

```
SELECT Sno,COUNT(*) FROM SC WHERE Grade>=80 GROUP BY Sno;
```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

- 

```

```

