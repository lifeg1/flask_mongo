from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# import os
#
app=Flask(__name__)
# basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY']='mysecretkey'
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+ os.path.join(basedir,'database.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#
#
# db=SQLAlchemy(app)
# Migrate(app,db)
