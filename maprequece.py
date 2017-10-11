# -*- coding: cp936 -*-
import pymongo
from bson.code import Code

client = pymongo.MongoClient('localhost:27017')
db = client['maimai_num']
collection = db['users']

# map函数的作用是遍历集合，调用emit函数将集合中userId、nick字段以键值对的形式传递给reduce函数
mapper = Code("""
function(){
    emit(this._id, this.all['data']);
}
""")

# reduce函数的作用对map函数传递过来的键值对进行处理, 每个<key, values>键值对中，key是userId字段的值，values是具有相同userId的nick的数组。由于我的程序中一个values的各个元素的值是相同的，所以没有对values进行遍历。
reducer = Code("""
function(key, values){
    var result = {key,values};
    return result;
}
""")

# 启动MapReduce, 将结果输出到seller_info这个集合中
result = collection.map_reduce(mapper, reducer, 'users2')

# 遍历seller_info集合，查看MapReduce结果
#for doc in db['papers2'].find():
#    print doc

