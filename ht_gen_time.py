# coding:utf-8
# @Author     : HT
# @Time       : 2022/12/6 9:00
# @File       : test.py
# @Software   : PyCharm

import datetime

import time
import  random
def gen_time(tuple1,tuple2,NUM):
    MINTIME = datetime.datetime(*tuple1)

    MAXTIME = datetime.datetime(*tuple2)

    mintime_ts = int(time.mktime(MINTIME.timetuple()))

    maxtime_ts = int(time.mktime(MAXTIME.timetuple()))

    random_ts_list=[]

    for RECORD in range(NUM):

        random_ts = random.randint(mintime_ts, maxtime_ts)
        # print(random_ts)
        random_ts_list.append(random_ts)
    random_ts_list.sort()
    RANDOMTIME_list=[]
    for random_ts in random_ts_list:
        RANDOMTIME = datetime.datetime.fromtimestamp(random_ts)
        RANDOMTIME_list.append(RANDOMTIME)
        # print (RANDOMTIME)
    return RANDOMTIME_list

if __name__=='__main__':
    gen_time((2006,8,6,8,14,59), (2022,12,6,9,0,0),1000)
    MINTIME = datetime.datetime(2006,8,6,8,14,59)

    MAXTIME = datetime.datetime(2022,12,6,9,0,0)

    mintime_ts = int(time.mktime(MINTIME.timetuple()))

    maxtime_ts = int(time.mktime(MAXTIME.timetuple()))

    random_ts_list=[]

    for RECORD in range(1000):

        random_ts = random.randint(mintime_ts, maxtime_ts)
        print(random_ts)
        random_ts_list.append(random_ts)
    random_ts_list.sort()
    RANDOMTIME_list=[]
    for random_ts in random_ts_list:
        RANDOMTIME = datetime.datetime.fromtimestamp(random_ts)
        RANDOMTIME_list.append(RANDOMTIME)
        print (RANDOMTIME)
