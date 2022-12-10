```mysql
DROP Table IF EXISTS Repair_Order
```

```mysql
CREATE Table Staff(
 Staff_Number int(6) primary key,
 Staff_Name varchar(8),
 Staff_Sex char(2) Default '男',
 Staff_Birth Date,
 Staff_Work_Type char(4),
 Check (Staff_Sex in ('男','女')),
 Check (Staff_Work_Type in ('维修','生产'))
)
```

```mysql
CREATE Table Mainboard(
 Mainboard_Number varchar(6) primary key,
 Mainboard_Cost int(8),
 Mainboard_Sale_Price int(8)
)
```

```mysql
CREATE Table SMT_U_Line(
 U_Line_Number varchar(10) primary key,
 U_Line_Operation_Status varchar(2) 
)
```

```mysql
CREATE Table Repair_Order(
 Repair_Order_Number int(4) primary key,
 Repair_Start_Time DATETIME,
 Repair_End_Time DATETIME,
 Staff_Number int(6),
 U_Line_Number varchar(10),
 Foreign Key(Staff_Number) references Staff(Staff_Number),
 Foreign Key(U_Line_Number) references SMT_U_Line(U_Line_Number) 
)
```

```mysql
CREATE Table Dispatch_Order(
 Dispatch_Order_Number int(8) primary key,
 Work_Plan_Start_Time DATETIME,
 Work_Plan_End_Time DATETIME,
 Work_Real_Start_Time DATETIME,
 Work_Real_End_Time DATETIME,
 Work_Real_Sum_Number int,
 Work_Real_Qualified_Number int,
 Work_Plan_Number int,
 Staff_Number int(6),
 U_Line_Number varchar(10),
 Mainboard_Number varchar(6),
 Foreign Key(Staff_Number) references Staff(Staff_Number),
 Foreign Key(U_Line_Number) references SMT_U_Line(U_Line_Number),
 Foreign Key(Mainboard_Number) references Mainboard(Mainboard_Number)
 )
```

```mysql
INSERT into SMT_U_Line (U_Line_Number, U_Line_Operation_Status ) values(%s,%s)
```

```mysql
INSERT into Mainboard (Mainboard_Number, Mainboard_Cost, Mainboard_Sale_Price ) values(%s,%s,%s)
```

```mysql
INSERT into Dispatch_Order (Dispatch_Order_Number, Work_Plan_Start_Time, Work_Plan_End_Time, Work_Real_Start_Time, Work_Real_End_Time, Work_Real_Sum_Number, Work_Real_Qualified_Number, Work_Plan_Number, Staff_Number, U_Line_Number, Mainboard_Number ) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
```

```mysql
INSERT into Repair_Order (Repair_Order_Number, Repair_Start_Time, Repair_End_Time, Staff_Number, U_Line_Number ) values(%s,%s,%s,%s,%s)
```

```mysql
INSERT into Staff (Staff_Number, Staff_Name, Staff_Sex, Staff_Birth, Staff_Work_Type ) values(%s,%s,%s,%s,%s)
```

```mysql

```

```mysql
CREATE VIEW 维修员工完成维修单(工号, 姓名, 已完成维修次数 )
AS Select Staff.Staff_Number, Staff_Name, count(*)
From staff ,Repair_Order Where (Repair_Order.Staff_Number=Staff.Staff_Number) and Staff_Work_Type='维修' and (Not Repair_End_Time='2000-01-01 01:00:00')
GROUP BY Staff.Staff_Number
```

```mysql
CREATE VIEW 生产员工完成派工单数(工号, 姓名, 已完成派工单数 )
AS Select Staff.Staff_Number, Staff.Staff_Name,  count(*)
From staff,Dispatch_Order Where (Dispatch_Order.Staff_Number=Staff.Staff_Number) and Staff_Work_Type='生产' and (Not Work_Real_End_Time='2000-01-01 01:00:00')
GROUP BY Staff.Staff_Number
```





```mysql
CREATE VIEW 主板视图(主板型号, 单件成本, 单件售价,总实际产量 ,总合格产量 ,总计划产量,合格率,生产完成率,总生产利润)
AS Select Mainboard.Mainboard_Number, Mainboard_Cost, Mainboard_Sale_Price, /SUM(Work_Real_Sum_Number)
SUM(Work_Real_Sum_Number), SUM(Work_Real_Qualified_Number),SUM(Work_Plan_Number),CONCAT(TRUNCATE(SUM(Work_Real_Qualified_Number)/SUM(Work_Real_Sum_Number) *100,2),'%') ,CONCAT(TRUNCATE(SUM(Work_Real_Sum_Number)/SUM(Work_Plan_Number) *100,2),'%') ,
(Mainboard_Sale_Price*SUM(Work_Real_Qualified_Number)-Mainboard_Cost*SUM(Work_Real_Sum_Number))
From Mainboard,Dispatch_Order WHERE Mainboard.Mainboard_Number=Dispatch_Order.Mainboard_Number GROUP BY Mainboard.Mainboard_Number
```





```mysql
CREATE VIEW 正在生产的派工单(派工单编号, 计划开始时间, 计划完成时间,实际开始时间 ,生产主板,生产进度 ,生产员工,生产线,生产线的状态)
AS Select Dispatch_Order_Number, Work_Plan_Start_Time, Work_Plan_End_Time,Work_Real_Start_Time,Mainboard_Number
,CONCAT(TRUNCATE(SUM(Work_Real_Sum_Number)/SUM(Work_Plan_Number) *100,2),'%'),Staff_Name,Dispatch_Order.U_Line_Number,U_Line_Operation_Status
From Dispatch_Order,Staff,SMT_U_Line WHERE (Dispatch_Order.Staff_Number=Staff.Staff_Number) and (Dispatch_Order.U_Line_Number=SMT_U_Line.U_Line_Number) and (Work_Real_End_Time='2000-01-01 01:00:00')
GROUP BY Dispatch_Order_Number
Order By U_Line_Operation_Status
```

```mysql
CREATE VIEW 正在维修的维修单(维修单编号, 维修开始时间 ,维修员工)
AS Select Repair_Order_Number,Repair_Start_Time,Staff_Name
From Repair_Order,Staff WHERE (Repair_Order.Staff_Number=Staff.Staff_Number) and  (Repair_End_Time='2000-01-01 01:00:00')
GROUP BY Repair_Order_Number
```





```mysql
CREATE VIEW 生产线生产视图(产线编号, 已完成生产次数 , 合格率,生产完成率)
AS Select SMT_U_Line.U_Line_Number,count(case when Dispatch_Order.Work_Plan_Start_Time then 1 end ),CONCAT(TRUNCATE(SUM(Work_Real_Qualified_Number)/SUM(Work_Real_Sum_Number) *100,2),'%') ,CONCAT(TRUNCATE(SUM(Work_Real_Sum_Number)/SUM(Work_Plan_Number) *100,2),'%')
From SMT_U_Line,Dispatch_Order WHERE (SMT_U_Line.U_Line_Number=Dispatch_Order.U_Line_Number)  and (NOT Work_Real_End_Time='2000-01-01 01:00:00')
GROUP BY SMT_U_Line.U_Line_Number
```

```mysql
CREATE VIEW 生产线维修视图(产线编号, 维修次数 )
AS Select SMT_U_Line.U_Line_Number,count(case when Repair_Order.Repair_Order_Number then 1 end )
From SMT_U_Line LEFT OUTER JOIN Repair_Order On (SMT_U_Line.U_Line_Number=Repair_Order.U_Line_Number)  and (NOT  Repair_End_Time='2000-01-01 01:00:00')
GROUP BY SMT_U_Line.U_Line_Number
```





```mysql
CREATE VIEW 主板单件生产时间(主板型号, 单件成本, 单件售价,单件生产时间,总实际产量 ,总合格产量 ,总计划产量,合格率,生产完成率,总生产利润)
AS Select Mainboard.Mainboard_Number, Mainboard_Cost, Mainboard_Sale_Price, /SUM(Work_Real_Sum_Number)
SUM(Work_Real_Sum_Number), SUM(Work_Real_Qualified_Number),SUM(Work_Plan_Number),CONCAT(TRUNCATE(SUM(Work_Real_Qualified_Number)/SUM(Work_Real_Sum_Number) *100,2),'%') ,CONCAT(TRUNCATE(SUM(Work_Real_Sum_Number)/SUM(Work_Plan_Number) *100,2),'%') ,
(Mainboard_Sale_Price*SUM(Work_Real_Qualified_Number)-Mainboard_Cost*SUM(Work_Real_Sum_Number))
From Mainboard,Dispatch_Order WHERE Mainboard.Mainboard_Number=Dispatch_Order.Mainboard_Number GROUP BY Mainboard.Mainboard_Number
```





```mysql
CREATE VIEW 生产员工的工作状态(员工工号,姓名,员工状态)
AS Select Staff.Staff_Number,Staff_Name,U_Line_Operation_Status
From Dispatch_Order,Staff WHERE (Dispatch_Order.Staff_Number=Staff.Staff_Number) and (Dispatch_Order.U_Line_Number=SMT_U_Line.U_Line_Number)
GROUP BY Staff.Staff_Number
```





```mysql
CREATE Function birthday(sage date)
returns boolean NOT DETERMINISTIC NO SQL
begin
   declare date_now date;
   declare bool boolean;
   set date_now = curdate();
   if month(sage)=12 and month(date_now)=1 then
      if week(replace(sage, year(sage), year(date_now)-1), 7) = week(date_now,7) then
         set bool = 1;
      else
         set bool = 0;
      end if;
   elseif month(date_now)=12 and month(sage)=1 then
      if week(replace(sage, year(sage), year(date_now)+1), 7) = week(date_now,7) then
         set bool = 1;
      else
         set bool = 0;
      end if;
   elseif month(sage)=2 and day(sage)=29 then
      if year(date_now)%4=0 then
         if week(replace(sage, year(sage), year(date_now)),7) = week(date_now,7) then
	    set bool = 1;
         else
	    set bool = 0;
         end if;
      else
         if week(concat_ws('-',year(curdate()),'03','01'),7) = week(date_now,7) then
	    set bool = 1;
         else
	    set bool = 0;
         end if;
      end if;
   else
      if week(replace(sage, year(sage), year(date_now)),7) = week(date_now,7) then
         set bool = 1;
      else
         set bool = 0;
      end if;
   end if;
   return bool;
end
```

```mysql
CREATE VIEW 本周生日员工(工号, 姓名, 出生日期 )
AS Select Staff_Number, Staff_Name,  Staff_Birth
From (select *, birthday(Staff_Birth) as bool from staff )as a where a.bool = 1 
```





```mysql
Select Avg(year(now())-year(Staff_Birth)+1)
From staff Where month(Staff_Birth)=month(now())
```





```mysql
CREATE VIEW 合格率大于96的生产线视图(产线编号, 合格率)
AS Select SMT_U_Line.U_Line_Number,CONCAT(TRUNCATE(SUM(Work_Real_Qualified_Number)/SUM(Work_Real_Sum_Number) *100,2),'%')
From SMT_U_Line,Dispatch_Order WHERE (SMT_U_Line.U_Line_Number=Dispatch_Order.U_Line_Number)  and (NOT Work_Real_End_Time='2000-01-01 01:00:00')
GROUP BY SMT_U_Line.U_Line_Number HAVING SUM(Work_Real_Qualified_Number)/SUM(Work_Real_Sum_Number)>=0.96
```

```mysql
mysqldump -h localhost -u root -p database_smt > Z:\doing\数据库系统\ht_sql\database\database_smt.sql
```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

```mysql

```

