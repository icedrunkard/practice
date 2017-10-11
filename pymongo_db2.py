# -*- coding: cp936 -*-
import pymongo
from bson.code import Code

client = pymongo.MongoClient('localhost:27017')
db = client['maimai_num2']

col4= db['users4__']
col4_=db['users']


s=set()
for i in col4.find():
    if not i['id'] in s:
        s.add(i['id'])
        col4_.insert(i)

print(len(s))
