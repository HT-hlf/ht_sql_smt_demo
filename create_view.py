# coding:utf-8
# @Author     : HT
# @Time       : 2022/12/7 8:52
# @File       : create_view.py
# @Software   : PyCharm


#导入模块
import pymysql
import random
import datetime
from ht_gen_time import gen_time
#创建连接
con=pymysql.connect(host='localhost',user='root',password='123456',database='database_smt',port=3306)
#创建游标对象
cur=con.cursor()

sql=[
# #维修员工信息视图 丢弃
# """CREATE VIEW 维修员工(工号, 姓名, 性别, 出生日期 )
# AS Select Staff_Number, Staff_Name, Staff_Sex, Staff_Birth
# From staff Where Staff_Work_Type='维修' """,

# #维修员工信息视图
# """CREATE VIEW 维修员工完成维修单(工号, 姓名, 已完成维修次数 )
# AS Select Staff.Staff_Number, Staff_Name, count(*)
# From staff ,Repair_Order Where (Repair_Order.Staff_Number=Staff.Staff_Number) and Staff_Work_Type='维修' and (Not Repair_End_Time='2000-01-01 01:00:00')
# GROUP BY Staff.Staff_Number """,

# #生产员工信息视图 丢弃
# """ CREATE VIEW 生产员工(工号, 姓名, 性别, 出生日期 )
# AS Select Staff_Number, Staff_Name, Staff_Sex, Staff_Birth
# From staff Where Staff_Work_Type='生产' """,
#
# #生产员工信息视图
# """ CREATE VIEW 生产员工完成派工单数(工号, 姓名, 已完成派工单数 )
# AS Select Staff.Staff_Number, Staff.Staff_Name,  count(*)
# From staff,Dispatch_Order Where (Dispatch_Order.Staff_Number=Staff.Staff_Number) and Staff_Work_Type='生产' and (Not Work_Real_End_Time='2000-01-01 01:00:00')
# GROUP BY Staff.Staff_Number """,

#查询各个主板生产总量 单件生产时间
# """CREATE VIEW 主板视图(主板型号, 单件成本, 单件售价,总实际产量 ,总合格产量 ,总计划产量,合格率,生产完成率,总生产利润)
# AS Select Mainboard.Mainboard_Number, Mainboard_Cost, Mainboard_Sale_Price, /SUM(Work_Real_Sum_Number)
# SUM(Work_Real_Sum_Number), SUM(Work_Real_Qualified_Number),SUM(Work_Plan_Number),CONCAT(TRUNCATE(SUM(Work_Real_Qualified_Number)/SUM(Work_Real_Sum_Number) *100,2),'%') ,CONCAT(TRUNCATE(SUM(Work_Real_Sum_Number)/SUM(Work_Plan_Number) *100,2),'%') ,
# (Mainboard_Sale_Price*SUM(Work_Real_Qualified_Number)-Mainboard_Cost*SUM(Work_Real_Sum_Number))
# From Mainboard,Dispatch_Order WHERE Mainboard.Mainboard_Number=Dispatch_Order.Mainboard_Number GROUP BY Mainboard.Mainboard_Number """,
# #查询正在生产的派工单 将员工号查询到员工姓名 生产线查询到生产线状态 并且按生产状态进行排序，故障的放在最后 在工厂的实时屏幕显示
# # CONCAT(TRUNCATE(SUM(Work_Real_Sum_Number)/SUM(Work_Plan_Number) *100,2),'%')
# """CREATE VIEW 正在生产的派工单(派工单编号, 计划开始时间, 计划完成时间,实际开始时间 ,生产主板,生产进度 ,生产员工,生产线,生产线的状态)
# AS Select Dispatch_Order_Number, Work_Plan_Start_Time, Work_Plan_End_Time,Work_Real_Start_Time,Mainboard_Number
# ,CONCAT(TRUNCATE(SUM(Work_Real_Sum_Number)/SUM(Work_Plan_Number) *100,2),'%'),Staff_Name,Dispatch_Order.U_Line_Number,U_Line_Operation_Status
# From Dispatch_Order,Staff,SMT_U_Line WHERE (Dispatch_Order.Staff_Number=Staff.Staff_Number) and (Dispatch_Order.U_Line_Number=SMT_U_Line.U_Line_Number) and (Work_Real_End_Time='2000-01-01 01:00:00')
# GROUP BY Dispatch_Order_Number
# Order By U_Line_Operation_Status""",
#
# """CREATE VIEW 正在维修的维修单(维修单编号, 维修开始时间 ,维修员工)
# AS Select Repair_Order_Number,Repair_Start_Time,Staff_Name
# From Repair_Order,Staff WHERE (Repair_Order.Staff_Number=Staff.Staff_Number) and  (Repair_End_Time='2000-01-01 01:00:00')
# GROUP BY Repair_Order_Number
# """,

#生产线 排除正在执行的派工单
# """CREATE VIEW 生产线生产视图(产线编号, 已完成生产次数 , 合格率,生产完成率)
# AS Select SMT_U_Line.U_Line_Number,count(case when Dispatch_Order.Work_Plan_Start_Time then 1 end ),CONCAT(TRUNCATE(SUM(Work_Real_Qualified_Number)/SUM(Work_Real_Sum_Number) *100,2),'%') ,CONCAT(TRUNCATE(SUM(Work_Real_Sum_Number)/SUM(Work_Plan_Number) *100,2),'%')
# From SMT_U_Line,Dispatch_Order WHERE (SMT_U_Line.U_Line_Number=Dispatch_Order.U_Line_Number)  and (NOT Work_Real_End_Time='2000-01-01 01:00:00')
# GROUP BY SMT_U_Line.U_Line_Number
# """,

#生产线 排除正在执行的派工单 需要考虑维修单没有的生产线 左外连接保留没有维修过的生产线
# """CREATE VIEW 生产线维修视图(产线编号, 维修次数 )
# AS Select SMT_U_Line.U_Line_Number,count(case when Repair_Order.Repair_Order_Number then 1 end )
# From SMT_U_Line LEFT OUTER JOIN Repair_Order On (SMT_U_Line.U_Line_Number=Repair_Order.U_Line_Number)  and (NOT  Repair_End_Time='2000-01-01 01:00:00')
# GROUP BY SMT_U_Line.U_Line_Number
# """,


# """CREATE VIEW 主板单件生产时间(主板型号, 单件成本, 单件售价,单件生产时间,总实际产量 ,总合格产量 ,总计划产量,合格率,生产完成率,总生产利润)
# AS Select Mainboard.Mainboard_Number, Mainboard_Cost, Mainboard_Sale_Price, /SUM(Work_Real_Sum_Number)
# SUM(Work_Real_Sum_Number), SUM(Work_Real_Qualified_Number),SUM(Work_Plan_Number),CONCAT(TRUNCATE(SUM(Work_Real_Qualified_Number)/SUM(Work_Real_Sum_Number) *100,2),'%') ,CONCAT(TRUNCATE(SUM(Work_Real_Sum_Number)/SUM(Work_Plan_Number) *100,2),'%') ,
# (Mainboard_Sale_Price*SUM(Work_Real_Qualified_Number)-Mainboard_Cost*SUM(Work_Real_Sum_Number))
# From Mainboard,Dispatch_Order WHERE Mainboard.Mainboard_Number=Dispatch_Order.Mainboard_Number GROUP BY Mainboard.Mainboard_Number """,
# #维修员工 根据当前时间判断维修人员的工作状态 用于实时安排任务 因为数据很难生成实时的，所以假设当前时间为 即用时间替换掉
# """CREATE VIEW 生产员工的工作状态(员工工号,姓名,员工状态)
# AS Select Staff.Staff_Number,Staff_Name,U_Line_Operation_Status
# From Dispatch_Order,Staff WHERE (Dispatch_Order.Staff_Number=Staff.Staff_Number) and (Dispatch_Order.U_Line_Number=SMT_U_Line.U_Line_Number)
# GROUP BY Staff.Staff_Number""",

# 判断本周生日的函数
# """create function birthday(sage date)
# returns boolean NOT DETERMINISTIC NO SQL
# begin
#    declare date_now date;
#    declare bool boolean;
#    set date_now = curdate();
#    if month(sage)=12 and month(date_now)=1 then
#       if week(replace(sage, year(sage), year(date_now)-1), 7) = week(date_now,7) then
#          set bool = 1;
#       else
#          set bool = 0;
#       end if;
#    elseif month(date_now)=12 and month(sage)=1 then
#       if week(replace(sage, year(sage), year(date_now)+1), 7) = week(date_now,7) then
#          set bool = 1;
#       else
#          set bool = 0;
#       end if;
#    elseif month(sage)=2 and day(sage)=29 then
#       if year(date_now)%4=0 then
#          if week(replace(sage, year(sage), year(date_now)),7) = week(date_now,7) then
# 	    set bool = 1;
#          else
# 	    set bool = 0;
#          end if;
#       else
#          if week(concat_ws('-',year(curdate()),'03','01'),7) = week(date_now,7) then
# 	    set bool = 1;
#          else
# 	    set bool = 0;
#          end if;
#       end if;
#    else
#       if week(replace(sage, year(sage), year(date_now)),7) = week(date_now,7) then
#          set bool = 1;
#       else
#          set bool = 0;
#       end if;
#    end if;
#    return bool;
# end""",
# """ select sno, sname, sage, ssex
# from (select *, birthday(sage) as bool from student) as a
# where a.bool = 1;"""
# #查询今天生日的员工 创建日期2022-12-7
# """CREATE VIEW 本周生日员工(工号, 姓名, 出生日期 )
# AS Select Staff_Number, Staff_Name,  Staff_Birth
# From (select *, birthday(Staff_Birth) as bool from staff )as a where a.bool = 1   """,

# 全部员工的平均年龄
# """Select Avg(year(now())-year(Staff_Birth)+1)
# From staff Where month(Staff_Birth)=month(now()) """,
    # mysql用now 相比于 getdate()

#生产线 查询合格率大于95%的生产线
"""CREATE VIEW 合格率大于96的生产线视图(产线编号, 合格率)
AS Select SMT_U_Line.U_Line_Number,CONCAT(TRUNCATE(SUM(Work_Real_Qualified_Number)/SUM(Work_Real_Sum_Number) *100,2),'%')
From SMT_U_Line,Dispatch_Order WHERE (SMT_U_Line.U_Line_Number=Dispatch_Order.U_Line_Number)  and (NOT Work_Real_End_Time='2000-01-01 01:00:00')
GROUP BY SMT_U_Line.U_Line_Number HAVING SUM(Work_Real_Qualified_Number)/SUM(Work_Real_Sum_Number)>=0.96
""",


# 查询正在生产并且故障的派工单  将派工单分配给其他生产线

]

try:
    # 执行sql
    for sql_ele in sql:
        cur.execute(sql_ele)
        #提交事务
        con.commit()
        print('插入成功')
except Exception as e:
    print(e)
    con.rollback()
    print('插入失败')