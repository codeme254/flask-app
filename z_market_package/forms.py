from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, Email, EqualTo, ValidationError
from z_market_package.models import User

class RegisterUserForm(FlaskForm):
    """
    Form for registering a user and creating their account
    """
    def validate_username(self, username_to_check):
        user = User.query.filter_by(prefered_username = username_to_check.data).first()
        if user:
            raise ValidationError("Username already exists, please try a different username")
    
    def validate_email_address(self, email_to_check):
        email = User.query.filter_by(email_address = email_to_check.data).first()
        if email:
            raise ValidationError("Email already exists, are you trying to login?????")

    first_name = StringField(label="Your Legal First Name:", validators=[Length(min=2), DataRequired()])
    last_name = StringField(label="Your Legal Last Name:", validators=[Length(min=2), DataRequired()])
    # age = NumberField(label="Your Age:")
    username = StringField(label="User Name:", validators=[Length(min=4), DataRequired()])
    email_address = StringField(label="Email Address:", validators=[Email(), Length(min=4), DataRequired()])
    password = PasswordField(label="Create Password:", validators=[Length(min=8), DataRequired()])
    confirm_password = PasswordField(label="Confirm Password:", validators=[Length(min=8), EqualTo('password'), DataRequired()])
    submit = SubmitField(label="Create Account")