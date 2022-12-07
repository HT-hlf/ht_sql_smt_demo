# coding:utf-8
# @Author     : HT
# @Time       : 2022/11/22 23:53
# @File       : create_data.py
# @Software   : PyCharm

#导入pymysql
import pymysql
#创建连接
con=pymysql.connect(host='localhost',user='root',password='123456',database='database_smt',port=3306)
#创建游标对象
cur=con.cursor()
#编写创建表的sql
# SMT_U_Line（U_Line_Number、U_Line_Operation_Status）
# Dispatch_Order（Dispatch_Order_Number、Work_Plan_Start_Time、Work_Plan_End_Time、Work_Real_Start_Time、Work_Real_End_Time、Work_Real_Sum_Number、Work_Real_Qualified_Number、Work_Plan_Number、Staff_Number、U_Line_Number、Mainboard_Number）
# Mainboard（Mainboard_Number、Mainboard_Cost、Mainboard_Sale_Price）
# Staff（Staff_Number、Staff_Name、Staff_Sex、Staff_Age、Staff_Work_Type）
# Repair_Order（Repair_Order_Number、Repair_Start_Time、Repair_End_Time、Staff_Number、U_Line_Number）

sql=[

"""
DROP TABLE IF EXISTS Repair_Order
""",
"""
DROP TABLE IF EXISTS Dispatch_Order
""",
"""
DROP TABLE IF EXISTS Staff 
""",
"""
DROP TABLE IF EXISTS Mainboard
""",
"""
DROP TABLE IF EXISTS SMT_U_Line 
""",
"""
    create table Staff(
     Staff_Number int(6) primary key,
     Staff_Name varchar(8),
     Staff_Sex char(2) Default '男',
     Staff_Birth Date,
     Staff_Work_Type char(4),
     Check (Staff_Sex in ('男','女')),
     Check (Staff_Work_Type in ('维修','生产'))
     )
""",
"""
    create table Mainboard(
     Mainboard_Number varchar(6) primary key,
     Mainboard_Cost int(8),
     Mainboard_Sale_Price int(8))
""",

"""
    create table SMT_U_Line(
     U_Line_Number varchar(10) primary key,
     U_Line_Operation_Status varchar(2)
    )
""",


"""
    create table Repair_Order(
     Repair_Order_Number int(4) primary key,
     Repair_Start_Time DATETIME,
     Repair_End_Time DATETIME,
     Staff_Number int(6),
     U_Line_Number varchar(10),
     Foreign Key(Staff_Number) references Staff(Staff_Number),
     Foreign Key(U_Line_Number) references SMT_U_Line(U_Line_Number)
     )
""",

"""
    create table Dispatch_Order(
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
""",
]
try:
    for sql_ele in sql:
        # 执行创建表的sql
        cur.execute(sql_ele)
        print('创建表成功')
except Exception as e:
    print(e)
    print('创建表失败')
finally:
    #关闭连接
    con.close()