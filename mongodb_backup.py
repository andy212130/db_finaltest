#python3
#mongodb.py
import pymongo
from pymongo import MongoClient
import random
from datetime import datetime
import time
client =MongoClient('127.0.0.1',27017) #資料庫連線
def creat_database():
    db = client['finaltest'] #建立資料庫
    #print(db)
    return db
#工廠資料表
def create_table_factory():
    factory = db['factory']
    factorylist = [{'id':"A",'owner':'Oa'},{'id':"B",'owner':'Ob'},{'id':"C",'owner':'Oc'}]
    factory.insert_many(factorylist)

    for fa in factory.find():
        print(fa)
    return factory
#感測器資料表
def creat_table_senser():

    senser = db['senser']
    senserlist = [{'id':'001','model':'DHT11','type':'tmp','place':'facA'},{'id':'002','model':'DHT22','type':'hum','place':'facA'},
            {'id':'003','model':'DHT11','type':'tmp','place':'facB'},{'id':'004','model':'DHT22','type':'hum','place':'facB'},
            {'id':'005','model':'DHT11','type':'tmp','place':'facC'},{'id':'006','model':'DHT22','type':'hum','place':'facC'}]
    senser.insert_many(senserlist)

    for se in senser.find():
        print(se)
    return senser
def create_table_data(type,data,s):
    global da
    try:
        da = db['Tdata']#建立Data資料表
    except Exception as e:
        print(e)
#    return Tdata
#將偵測資料存入資料庫
#def newdata(type,data,s):
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if type == 't':
        unit = 'C'
        if data >= 40:
            status='overheat'
        else:
            status='common'
    else:
        unit = '%'
        status = 'common'
    data=str(data)
    next_data={'senser':s,'data':data,'status':status,'date':date}
    print(next_data)
    da.insert_one(next_data)
def main():
    while(1):
        t1 = random.uniform(33.0,42.0)
        h1 = random.uniform(40.0,60.0)
        t2 = random.uniform(33.0,42.0)
        h2 = random.uniform(40.0,60.0)
        t3 = random.uniform(33.0,42.0)
        h3 = random.uniform(40.0,60.0)
        create_table_data('t',t1,'001')
        create_table_data('h',h1,'002')
        create_table_data('t',t2,'003')
        create_table_data('h',h2,'004')
        create_table_data('t',t3,'005')
        create_table_data('h',h3,'006')
        time.sleep(5)    #每五秒感測一次

if __name__ == '__main__':
    #db = creat_database()
    try:
        db = creat_database()
        fa = create_table_factory()
        se = creat_table_senser()
    except Exception as e:
        print(e)
    main()
