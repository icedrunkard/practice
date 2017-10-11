# -*- coding: utf-8 -*-
import pymongo
from bson.code import Code
import re
client = pymongo.MongoClient('115.159.49.35:27017')
db = client['cnki']
col= db['papers2']
lines=[]
ins=col.find({'school_name':re.compile('清华')},limit=1)
print type(ins)
for item in ins:
    lines.append(item)
    print item
    if len(lines)>10:
        break
    
