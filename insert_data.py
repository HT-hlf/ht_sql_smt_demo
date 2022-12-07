# coding:utf-8
# @Author     : HT
# @Time       : 2022/12/1 16:24
# @File       : insert_data.py
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


#编写插入数据的sql
# SMT_U_Line (U_Line_Number, U_Line_Operation_Status )
# Dispatch_Order (Dispatch_Order_Number, Work_Plan_Start_Time, Work_Plan_End_Time, Work_Real_Start_Time, Work_Real_End_Time, Work_Real_Sum_Number, Work_Real_Qualified_Number, Work_Plan_Number, Staff_Number, U_Line_Number, Mainboard_Number )
# Mainboard (Mainboard_Number, Mainboard_Cost, Mainboard_Sale_Price )
# Staff (Staff_Number, Staff_Name, Staff_Sex, Staff_Birth, Staff_Work_Type )
# Repair_Order (Repair_Order_Number, Repair_Start_Time, Repair_End_Time, Staff_Number, U_Line_Number )
#生产线
sql='insert into SMT_U_Line (U_Line_Number, U_Line_Operation_Status ) values(%s,%s)'
SMT_list=[]
smt_status=['生产','生产','生产','生产','生产','故障']
SMT_U_Line_NUM=99
SMT_U_Line_List=['SMTLine_'+str(i).zfill(2) for i in range(SMT_U_Line_NUM)]
for i in SMT_U_Line_List:
    SMT_list.append((i,smt_status[random.randint(0,5)]))
try:
    # 执行sql
    cur.executemany(sql,SMT_list)
    #提交事务
    con.commit()
    print('插入成功')
except Exception as e:
    print(e)
    con.rollback()
    print('插入失败')


#员工
# Staff (Staff_Number, Staff_Name, Staff_Sex, Staff_Birth, Staff_Work_Type )
sex=['男','男','女']
Staff_Work_Type=['维修','生产']
sql='insert into Staff (Staff_Number, Staff_Name, Staff_Sex, Staff_Birth, Staff_Work_Type ) values(%s,%s,%s,%s,%s)'
Staff_NUM=SMT_U_Line_NUM+10
Staff_num_List=[str(i).zfill(6) for i in range(Staff_NUM)]
staff_birth_list=gen_time((1980,8,6,8,14,59), (2001,12,6,9,0,0),Staff_NUM)
Staff_list=[]
count_staff=0
name_first='赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康伍元卜顾孟平黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴谈宋茅庞熊纪舒屈项祝董梁杜阮蓝闵席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田樊胡凌霍虞万支柯昝管卢莫经房裘缪干解应宗丁宣贲邓郁单杭洪包诸左石崔吉钮龚程嵇邢滑裴陆荣翁荀羊於惠甄曲家封芮羿储靳汲邴糜松井段富巫乌焦巴弓牧隗山谷车侯宓蓬全郗班仰秋仲伊宫'
name_second='赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康伍元卜顾孟平黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴谈宋茅庞熊纪舒屈项祝董梁杜阮蓝闵席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田樊胡凌霍虞万支柯昝管卢莫经房裘缪干解应宗丁宣贲邓郁单杭洪包诸左石崔吉钮龚程嵇邢滑裴陆荣翁荀羊於惠甄曲家封芮羿储靳汲邴糜松井段富巫乌焦巴弓牧隗山谷车侯宓蓬全郗班仰秋仲伊宫'
name_second=sorted(name_second,reverse=True)
for i in Staff_num_List:
    if count_staff<=SMT_U_Line_NUM:
        Staff_list.append((str(count_staff).zfill(6),name_first[count_staff]+name_second[count_staff],sex[random.randint(0,2)],staff_birth_list[count_staff],Staff_Work_Type[1]))
    else:
        Staff_list.append((str(count_staff).zfill(6),name_first[count_staff]+name_second[count_staff], sex[random.randint(0, 2)],staff_birth_list[count_staff], Staff_Work_Type[0]))
    count_staff+=1
# Staff_list=[('000106', '甄', '女', '2022-11-30-12-33', '维修')]
print(Staff_list)
try:
    # 执行sql
    cur.executemany(sql,Staff_list)
    #提交事务
    con.commit()
    print('插入成功')
except Exception as e:
    print(e)
    con.rollback()
    print('插入失败')

# 主板
# Mainboard (Mainboard_Number, Mainboard_Cost, Mainboard_Sale_Price )
A_Z='QWERTYUIOPASDFGHJKLZXCVBNM'
PCB_name_list=['PCB_A'+A_Z[i] for i in range(26)]

sql='insert into Mainboard (Mainboard_Number, Mainboard_Cost, Mainboard_Sale_Price ) values(%s,%s,%s)'

Mainboard_list=[]

for Mainboard in PCB_name_list:
    cost=random.randint(500, 1000)
    Mainboard_list.append((Mainboard,cost,cost+random.randint(600,1200)))


try:
    # 执行sql
    cur.executemany(sql,Mainboard_list)
    #提交事务
    con.commit()
    print('插入成功')
except Exception as e:
    print(e)
    con.rollback()
    print('插入失败')

#派工单
sql='insert into Dispatch_Order (Dispatch_Order_Number, ' \
    'Work_Plan_Start_Time, ' \
    'Work_Plan_End_Time, ' \
    'Work_Real_Start_Time, ' \
    'Work_Real_End_Time, ' \
    'Work_Real_Sum_Number, ' \
    'Work_Real_Qualified_Number, ' \
    'Work_Plan_Number, ' \
    'Staff_Number, ' \
    'U_Line_Number, ' \
    'Mainboard_Number ) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
Dispatch_Order_list=[]
Repair_Order_list=[]
smt_status=['生产','生产','生产','生产','生产','闲置','故障']
count=0
RANDOMTIME_list=gen_time((2004,8,6,8,14,59), (2022,12,6,9,0,0),70000)
for i in range(600):
    count_smt=count%SMT_U_Line_NUM
    count_staff = count % (SMT_U_Line_NUM+10)
    random1=random.randint(500, 1500)
    if count<500:
        if count_staff<=SMT_U_Line_NUM:
            Dispatch_Order_list.append((str(count).zfill(8),
                                               RANDOMTIME_list[100*(count+1)],
                                               RANDOMTIME_list[100*(count+2)-50],
                                               RANDOMTIME_list[100 * (count + 1)+random.randint(-25,25)],
                                               RANDOMTIME_list[100*(count+2)-50+random.randint(-25,25)],
                                               random1,
                                               random1-random.randint(0, 100),
                                               random1+random.randint(0,50),
                                               Staff_num_List[count_staff],
                                               SMT_U_Line_List[count_smt],
                                               PCB_name_list[random.randint(0,25)]
                                               ))
        else:
            Repair_Order_list.append((str(count).zfill(4),
                                        RANDOMTIME_list[100 * (count + 1)],
                                        RANDOMTIME_list[100 * (count + 2) - 50],
                                        Staff_num_List[count_staff],
                                        SMT_U_Line_List[count_smt],
                                        ))
    else:
        print('ht')
        # if count_staff<=SMT_U_Line_NUM:
        if random.randint(0,6):
            Dispatch_Order_list.append((str(count).zfill(8),
                                               RANDOMTIME_list[100*(count+1)],
                                               RANDOMTIME_list[100*(count+2)-50],
                                               RANDOMTIME_list[100 * (count + 1)+random.randint(-25,25)],
                                               datetime.datetime(2000, 1, 1, 1, 00, 00),
                                               random1,
                                               random1-random.randint(0, 100),
                                               random1+random.randint(100,500),
                                               Staff_num_List[count_staff],
                                               SMT_U_Line_List[count_smt],
                                               PCB_name_list[random.randint(0,25)]
                                               ))
        else:
            Repair_Order_list.append((str(count).zfill(4),
                                        RANDOMTIME_list[100 * (count + 1)],
                                        datetime.datetime(2000, 1, 1, 1, 00, 00),
                                        Staff_num_List[count_staff],
                                        SMT_U_Line_List[count_smt],
                                        ))
    count+=1
# print(Dispatch_Order_list)
try:
    # 执行sql
    cur.executemany(sql,Dispatch_Order_list)
    #提交事务
    con.commit()
    print('插入成功')
except Exception as e:
    print(e)
    con.rollback()
    print('插入失败')



#维修单
# Repair_Order (Repair_Order_Number, Repair_Start_Time, Repair_End_Time, Staff_Number, U_Line_Number )
sql='insert into Repair_Order (Repair_Order_Number, ' \
    'Repair_Start_Time, ' \
    'Repair_End_Time,' \
    ' Staff_Number,' \
    ' U_Line_Number ) values(%s,%s,%s,%s,%s)'

# print(Repair_Order_list)
try:
    # 执行sql
    cur.executemany(sql,Repair_Order_list)
    #提交事务
    con.commit()
    print('插入成功')
except Exception as e:
    print(e)
    con.rollback()
    print('插入失败')
finally:
    #关闭连接
    con.close()