#导入pymysql
import pymysql
#创建连接
con=pymysql.connect(host='localhost',database='python_db',user='root',password='123456',port=3306)
#创建游标对象
cur=con.cursor()
#编写查询的sql
sql='select * from t_student where score=99.8'
#执行sql
try:
    cur.execute(sql)
    #处理结果集
    student=cur.fetchone()
    print(student)
    sno=student[0]
    sname=student[1]
    age=student[2]
    score=student[3]
    print('sno:',sno,'sname:',sname,'age:',age,'score:',score)
except Exception as e:
    print(e)
    print('查询所有数据失败')
finally:
    #关闭连接
    con.close()