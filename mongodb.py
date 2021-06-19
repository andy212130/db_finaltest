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
#工廠資料表
def create_table_factory():
    factory = db['factory']
    factorylist = [{'id':"A",'owner':'Oa'},{'id':"B",'owner':'Ob'},{'id':"C",'owner':'Oc'}]
    factory.insert_many(factorylist)

    for fa in factory.find():
        print(fa)
#感測器資料表
def creat_table_senser():

    senser = db['senser']
    senserlist = [{'id':'001','model':'DHT11','type':'tmp','place':'facA'},{'id':'002','model':'DHT22','type':'hum','place':'facA'},
            {'id':'003','model':'DHT11','type':'tmp','place':'facB'},{'id':'004','model':'DHT22','type':'hum','place':'facB'},
            {'id':'005','model':'DHT11','type':'tmp','place':'facC'},{'id':'006','model':'DHT22','type':'hum','place':'facC'}]
    senser.insert_many(senserlist)

    for se in senser.find():
        print(se)
def create_table_data():
    Tdata = db['Tdata']   #建立Data資料表
    return Tdata
#將偵測資料存入資料庫
def newdata(type,data,s):
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
    da.insert_one(next_data)
def main():
    while(1):
        t1 = random.uniform(33.0,42.0)
        h1 = random.uniform(40.0,60.0)
        t2 = random.uniform(33.0,42.0)
        h2 = random.uniform(40.0,60.0)
        t3 = random.uniform(33.0,42.0)
        h3 = random.uniform(40.0,60.0)
        newdata('t',t1,'001')
        newdata('h',h1,'002')
        newdata('t',t2,'003')
        newdata('h',h2,'004')
        newdata('t',t3,'005')
        newdata('h',h3,'006')
        time.sleep(5)    #每五秒感測一次

if __name__ == '__main__':
    try:
        db = creat_database()
        fa = create_table_factory()
        se = creat_table_senser()
        da = create_table_data()
    except Exception as e:
        print(e)
    main()
