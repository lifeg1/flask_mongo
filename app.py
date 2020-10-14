from mycode import app #mycode is package as it contains __init__.py
                        #and init file contains config and Flask,Db thing over there
from flask import render_template,url_for,redirect,request,flash
from mycode.forms import Add_Product_Form
# from mycode.utl import sqlcon
from  pymongo import MongoClient,errors
myclient = MongoClient("mongodb+srv://user:life12@cluster0.wlvs0.mongodb.net/prddatabase?retryWrites=true&w=majority")
mydb=myclient.prddatabase
mycol=mydb.product




@app.route('/')
def index():
    return '<h1> append HOME in URL<h1>'

@app.route('/add_product',methods=['GET','POST'])
def add_product():
    print('Inside ADD')
    form=Add_Product_Form()
    if form.validate_on_submit():
        try:
            print('Inside form validate')
            rec_dect={"_id":form.prd_code.data,"prd_name":form.prd_name.data,"unit":form.unit.data,"cat":form.cat_name.data}
            print(rec_dect)
            x = mycol.insert_one(rec_dect)
            return redirect(url_for('list_prd'))
        except errors.DuplicateKeyError:
            err="Duplicate PRODUCT KEY"
            print(err)
            flash(f'ERROR IN ADDING PRODUCT:{err}')
            return render_template('add_product.html',form=form)
    return render_template('add_product.html',form=form)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/list')
def list_prd():
    prd = mycol.find({},{ "_id": 1,"prd_name": 1 ,"unit":1,'cat':1})
    print(prd)
    return render_template('list.html',prd=prd)


@app.route('/sales')
def sales():
    return render_template('add_sales.html')

@app.route('/edit/<string:cat>/<string:pcode>/',methods=['GET','POST'])
def edit_product(cat,pcode):
        myq={ "_id":pcode}
        rec_old= mycol.find_one(myq,{ "_id": 1, "prd_code": 1, "prd_name": 1 ,"unit":1,'cat':1})
        print(rec_old)
        form=Add_Product_Form()
        if form.validate_on_submit():
            try:
                print('Inside form validate')
                rec_dect={"$set":{"prd_code":form.prd_code.data,"prd_name":form.prd_name.data,"unit":form.unit.data,"cat":form.cat_name.data}}
                print(rec_dect)
                myq2={ "_id":pcode}
                x = mycol.update_one(myq2, rec_dect)
                return redirect(url_for('list_prd'))
            except errors.DuplicateKeyError:
                err="Duplicate PRODUCT KEY"
                print(err)
                flash(f'ERROR IN ADDING PRODUCT:{err}')
                return render_template('edit_product.html',form=form,rec=rec_old)
        print('inside edit product ',cat,pcode)
        return render_template('edit_product.html',form=form,rec=rec_old)


@app.route('/delete/<string:cat>/<string:pcode>/')
def delete_product(cat,pcode):
    print('inside delete ',cat,pcode)
    mycol.delete_one({"_id":pcode})
    return redirect(url_for('list_prd'))

if __name__=='__main__':
    app.run(host='127.0.0.1',port=8000,debug=True)
    # serve(app, host='127.0.0.1', port=5000)
