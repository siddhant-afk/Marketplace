from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,Email,EqualTo,DataRequired,ValidationError
from .models import User

class RegisterForm(FlaskForm):

    def validate_username(self,username_to_check):
        if User.query.filter_by(username=username_to_check.data).first():
            raise ValidationError("This username has already been taken.")
        
    def validate_email_address(self,email_to_check):
        if User.query.filter_by(email_address=email_to_check.data).first():
            raise ValidationError("This email is already linked to an account.")
        
        

    username = StringField(label="Username :",validators=[Length(min=2,max=30),DataRequired()])
    email_address = StringField(label="Email :",validators=[Email(),DataRequired()])
    password1 = PasswordField(label="Password :",validators=[Length(min=6),DataRequired()])
    password2 = PasswordField(label="Confirm Password",validators=[EqualTo('password1'),DataRequired()])
    submit = SubmitField(label='Submit')