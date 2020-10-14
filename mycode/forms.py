from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,SelectField
from wtforms.validators import (DataRequired,Length,NumberRange,Optional)

class Add_Product_Form(FlaskForm):
    prd_code=StringField('Product CodeNo',[DataRequired()])
    prd_name=StringField('Product Name',[DataRequired()])
    unit=SelectField('Unit',[DataRequired()],choices=[('Box','Box'),('SqMtr','SqMtr'),('Litre','litre')])
    # open_stock=IntegerField('Opening Stock',[NumberRange(min=0)])
    # pur_rate=IntegerField('Purchase Rate',[NumberRange(min=0)])
    cat_name=SelectField('Group/Category Name',[DataRequired()],choices=[('Tiles','Tiles'),('Marbel','Marbel'),('Paint','Paint')])
    # min_alert_lvl=IntegerField('Min Alert Level',validators=[Optional(),NumberRange(min=0,message='Numeric value only')])
    submit=SubmitField("Add Product")
