from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterUserForm(FlaskForm):
    """
    Form for registering a user and creating their account
    """
    first_name = StringField(label="Your Legal First Name:")
    last_name = StringField(label="Your Legal Last Name:")
    # age = NumberField(label="Your Age:")
    username = StringField(label="User Name:")
    email_address = StringField(label="Email Address:")
    password = PasswordField(label="Create Password:")
    confirm_password = PasswordField(label="Confirm Password:")
    submit = SubmitField(label="Create Account")