# -*- coding: cp936 -*-
import pymongo
from bson.code import Code

client = pymongo.MongoClient('localhost:27017')
db = client['maimai_num']
collection = db['users']

# map�����������Ǳ������ϣ�����emit������������userId��nick�ֶ��Լ�ֵ�Ե���ʽ���ݸ�reduce����
mapper = Code("""
function(){
    emit(this._id, this.all['data']);
}
""")

# reduce���������ö�map�������ݹ����ļ�ֵ�Խ��д���, ÿ��<key, values>��ֵ���У�key��userId�ֶε�ֵ��values�Ǿ�����ͬuserId��nick�����顣�����ҵĳ�����һ��values�ĸ���Ԫ�ص�ֵ����ͬ�ģ�����û�ж�values���б�����
reducer = Code("""
function(key, values){
    var result = {key,values};
    return result;
}
""")

# ����MapReduce, ����������seller_info���������
result = collection.map_reduce(mapper, reducer, 'users2')

# ����seller_info���ϣ��鿴MapReduce���
#for doc in db['papers2'].find():
#    print doc

