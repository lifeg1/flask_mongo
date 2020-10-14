from  pymongo import MongoClient
import pymongo
myclient = MongoClient("mongodb+srv://user:life12@cluster0.wlvs0.mongodb.net/prddatabase?retryWrites=true&w=majority")
mydb=myclient.prddatabase
mycol=mydb.product
print("-------------------------------------------------------------------------------------------")
# try:
mypip=[{ "$group" : {"_id": "$cat","num_total":{"$sum":1}}}]
ss=mycol.aggregate(mypip)
print(dict(ss))
print(type(ss))
for i in ss:
    print("insksns")
    print(i)
# except Exception as e:
#     print("Other Exception",e)
