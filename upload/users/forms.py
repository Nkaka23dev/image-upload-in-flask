from flask_wtf import FlaskForm 
from flask_wtf.file import FileField,FileRequired,FileAllowed
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,EqualTo,ValidationError
from upload.models import User

class CreateAccount(FlaskForm):
    name=StringField('Username',
                 validators=[DataRequired(),Length(min=5,max=30)])
    password=PasswordField('Password',validators=[DataRequired()])
    comfirm_password=PasswordField('Comfirm Password',validators=[EqualTo('password')])
    profile=FileField('Profile',validators=[FileAllowed(['png','jpeg','gif','jpg'])])
    submit=SubmitField('Submit')

    def validate_name(self,name):
        user=User.query.filter_by(name=name.data).first()
        if user:
           raise ValidationError('that name was taken ','danger')

class LoginForm(FlaskForm):
    name=StringField('Username',
                 validators=[DataRequired(),Length(min=5,max=30)])
    password=PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField('Login')