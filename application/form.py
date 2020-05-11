from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,DateField,IntegerField, ValidationError, validators
from wtforms.validators import DataRequired
from wtforms.validators import NumberRange, length
from wtforms.fields.html5 import DateField

class RegisterForm(FlaskForm):
    dep_city = StringField("Departure City", validators=[DataRequired(), length(min=2,max=15)])
    dep_date = DateField("Departure Date (YYYY-MM-DD)", validators= [DataRequired()])
    des1 = StringField("First Destination", validators=[DataRequired(), length(min=2,max=15)])
    dur1 = IntegerField("Number of days at destionation:", validators=[DataRequired(), NumberRange(min=1, max=14)])
    des2 = StringField("Second Destination", validators=[DataRequired(), length(min=2,max=15)])
    dur2 = IntegerField("Number of days at destionation:", validators=[DataRequired(), NumberRange(min=1, max=14)])
    des3 = StringField("Third Destination", validators= [length(min=2,max=15)])
    dur3 = IntegerField("Number of days at destionation:", validators=[NumberRange(min=1, max=14)])
    des4 = StringField("Fourth Destination", validators= [length(min=2,max=15)])
    dur4 = IntegerField("Number of days at destionation:", validators=[NumberRange(min=1, max=14)])

    submit = SubmitField("Generate")


