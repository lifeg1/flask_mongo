from flask import Flask,jsonify
from flask_restful import Resource,Api
app2=Flask(__name__)
api=Api(app2)
from  pymongo import MongoClient,errors
myclient = MongoClient("mongodb+srv://user:life12@cluster0.wlvs0.mongodb.net/prddatabase?retryWrites=true&w=majority")
mydb=myclient.prddatabase
mycol=mydb.product

class Product(Resource):
    def get(self):
        mypip=[{ "$group" : {"_id": "$cat","num_total":{"$sum":1}}}]
        ss=mycol.aggregate(mypip)
        return list(ss)


api.add_resource(Product,'/')
if __name__=='__main__':
    app2.run(debug=True)
