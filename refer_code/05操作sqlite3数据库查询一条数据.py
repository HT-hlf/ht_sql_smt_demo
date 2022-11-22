#导入模块
import sqlite3
#创建连接
con=sqlite3.connect('D:/sqlite3实例/demo.db')
#创建游标对象
cur=con.cursor()
#创建查询sql
sql='select * from t_person'
try:
    cur.execute(sql)
    #获取结果集，获取一条数据
    person=cur.fetchone()
    print(person)

except Exception as e:
    print(e)
    print('查询所有数据失败')
finally:
    #关闭游标
    cur.close()
    #关闭连接
    con.close()
