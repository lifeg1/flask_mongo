from  pymongo import MongoClient
myclient = MongoClient("mongodb+srv://user:life12@cluster0.wlvs0.mongodb.net/prddatabase?retryWrites=true&w=majority")
# myclient=MongoClient('127.0.0.1',27017)
# mydb = myclient["prddatabase"]
mydb=myclient.prddatabase
print(mydb.list_collection_names())

# mycol = mydb["product"]            # collection or table
mycol=mydb.product

mydict = { "prd_code": "p101", "prd_name": "Wall Tiles" ,"unit":"box"}
# x = mycol.insert_one(mydict)

x = mycol.find({},{ "_id": 0, "prd_code": 1, "prd_name": 1 ,"unit":1})
for i in x:
    print(i)
