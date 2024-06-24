from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField,DecimalField,SelectField, DateField, TimeField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError,NumberRange
from rs4.models import *


import psycopg2
from prettytable import PrettyTable

from bs4 import BeautifulSoup

class RegisterStudentForm(FlaskForm):
    def validate_username(self, username_to_check):

        html_input_string = str(username_to_check)

        soup = BeautifulSoup(html_input_string, 'html.parser')

        value = soup.input['value']

        cursor.execute("SELECT COUNT(*) FROM student WHERE username = %s", (value,))
        user = cursor.fetchone()[0]

        if user:
            
            raise ValidationError('Username already exists! Please try a different username')
    def validate_email(self, email_to_check):
         
        html_input_string = str(email_to_check)

        soup = BeautifulSoup(html_input_string, 'html.parser')

        value = soup.input['value']
        cursor.execute("SELECT COUNT(*) FROM student WHERE email = %s",(value,))
        user = cursor.fetchone()[0]
        if user:
            raise ValidationError('Email address already exists! Please try a different email address') 
        
    def validate_roll(self, username_to_check):

        html_input_string = str(username_to_check)

        soup = BeautifulSoup(html_input_string, 'html.parser')

        value = soup.input['value']

        cursor.execute("SELECT COUNT(*) FROM student WHERE roll = %s", (value,))
        user = cursor.fetchone()[0]

        if user:
            raise ValidationError('Roll Number already exists!! Try again.')
        
    name = StringField(label='Name:', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    roll = StringField(label='Roll No:',validators=[Length(min=9, max=9), DataRequired()])
    dept = StringField(label='Department Name:',validators=[Length(min=1, max=30), DataRequired()])
    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

class EditStudentForm(FlaskForm):
         
    name = StringField(label='Name:', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    submit = SubmitField(label='Update Profile')
    
    
class RegisterParticipantForm(FlaskForm):
    def validate_username(self, username_to_check):
         
        html_input_string = str(username_to_check)

        soup = BeautifulSoup(html_input_string, 'html.parser')

        value = soup.input['value']
        cursor.execute("SELECT COUNT(*) FROM participant WHERE username = %s", (value,))
        user = cursor.fetchone()[0]
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email(self, email_to_check):
         
        html_input_string = str(email_to_check)

        soup = BeautifulSoup(html_input_string, 'html.parser')

        value = soup.input['value']
        cursor.execute("SELECT COUNT(*) FROM participant WHERE email = %s",(value,))
        user = cursor.fetchone()[0]
        if user:
            raise ValidationError('Email address already exists! Please try a different email address') 

    name = StringField(label='Name:', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    college_name = StringField(label='College Name:', validators=[Length(min=2, max=30), DataRequired()])
    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    address = StringField(label='Address:', validators=[Length(min=2, max=30), DataRequired()])
    contact = StringField(label='Contact No:', validators=[Length(min=10, max=10), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

class EditParticipantForm(FlaskForm):

    name = StringField(label='Name:', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    college_name = StringField(label='College Name:', validators=[Length(min=2, max=30), DataRequired()])
    address = StringField(label='Address:', validators=[Length(min=2, max=30), DataRequired()])
    contact = StringField(label='Contact No:', validators=[Length(min=10, max=10), DataRequired()])
    submit = SubmitField(label='Update Profile')


class RegisterOrganizerForm(FlaskForm):
    def validate_username(self, username_to_check):
         
        html_input_string = str(username_to_check)

        soup = BeautifulSoup(html_input_string, 'html.parser')

        value = soup.input['value']
        cursor.execute("SELECT COUNT(*) FROM organizer WHERE username = %s", (value,))
        user = cursor.fetchone()[0]
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email(self, email_to_check):
         
        html_input_string = str(email_to_check)

        soup = BeautifulSoup(html_input_string, 'html.parser')

        value = soup.input['value']
        cursor.execute("SELECT COUNT(*) FROM organizer WHERE email = %s",(value,))
        user = cursor.fetchone()[0]
        if user:
            raise ValidationError('Email address already exists! Please try a different email address')

    name = StringField(label='Name:', validators=[Length(min=2, max=30), DataRequired()])
    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

class EditOrganizerForm(FlaskForm):

    name = StringField(label='Name:', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    submit = SubmitField(label='Update Profile')

class CreateEventForm(FlaskForm):
    def validate_event_name(self, username_to_check):
         
        html_input_string = str(username_to_check)

        soup = BeautifulSoup(html_input_string, 'html.parser')

        value = soup.input['value']
        cursor.execute("SELECT COUNT(*) FROM event WHERE event_name = %s", (value,))
        user = cursor.fetchone()[0]
        if user:
            raise ValidationError('Event already exists! Please try a different event name')
        
    event_name = StringField(label='Event Name',validators=[Length(min=2,max=30),DataRequired()])
    date = DateField(label='Date', format='%Y-%m-%d', validators=[DataRequired()])
    time = TimeField(label='Time', validators=[DataRequired()])
    description = StringField(label='Description',validators=[DataRequired()])
    first_prize_amt = StringField(label='First Prize',validators=[DataRequired()])
    second_prize_amt = StringField(label='Second Prize',validators=[DataRequired()])
    third_prize_amt = StringField(label='Third Prize',validators=[DataRequired()])
    submit = SubmitField(label="Create Event") 
    
class AdminCreateEventForm(FlaskForm):
    def validate_org_name(self, username_to_check):
         
        html_input_string = str(username_to_check)
        soup = BeautifulSoup(html_input_string, 'html.parser')

        value = soup.input['value']
        cursor.execute("SELECT COUNT(*) FROM organizer WHERE username = %s", (value,))
        user = cursor.fetchone()[0]
        if user:
            pass    
        else:
            raise ValidationError('Username does not exists! Please try a different username')
        
    def validate_event_name(self, username_to_check):
         
        html_input_string = str(username_to_check)

        soup = BeautifulSoup(html_input_string, 'html.parser')

        value = soup.input['value']
        cursor.execute("SELECT COUNT(*) FROM event WHERE event_name = %s", (value,))
        user = cursor.fetchone()[0]
        if user:
            raise ValidationError('Event already exists! Please try a different event name')
        
    event_name = StringField(label='Event Name',validators=[Length(min=2,max=30),DataRequired()])
    date = DateField(label='Date', format='%Y-%m-%d', validators=[DataRequired()])
    time = TimeField(label='Time', validators=[DataRequired()])
    description = StringField(label='Description',validators=[DataRequired()])
    org_name = StringField(label='Organizer',validators=[DataRequired()])
    first_prize_amt = StringField(label='First Prize',validators=[DataRequired()])
    second_prize_amt = StringField(label='Second Prize',validators=[DataRequired()])
    third_prize_amt = StringField(label='Third Prize',validators=[DataRequired()])
    submit = SubmitField(label="Create Event") 



class RegisterStudent_EventForm(FlaskForm):
    def validate_username(self, username_to_check):
         
        html_input_string = str(username_to_check)

        soup = BeautifulSoup(html_input_string, 'html.parser')

        value = soup.input['value']
        cursor.execute("SELECT COUNT(*) FROM student WHERE username = %s", (value,))
        user = cursor.fetchone()[0]
        if user:
            pass
        else:
            raise ValidationError('Student does not exists! Please try a different username')
        
    def validate_event_name(self, username_to_check):
         
        html_input_string = str(username_to_check)

        soup = BeautifulSoup(html_input_string, 'html.parser')

        value = soup.input['value']
        cursor.execute("SELECT COUNT(*) FROM event WHERE event_name = %s", (value,))
        user = cursor.fetchone()[0]
        if user:
            pass
        else:
            raise ValidationError('Event does not exists! Please try a different event name')
        
    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    event_name = StringField(label='Event Name',validators=[Length(min=2,max=30),DataRequired()])
    submit = SubmitField(label="Add") 
    
class RegisterParticipant_EventForm(FlaskForm):
    def validate_username(self, username_to_check):
         
        html_input_string = str(username_to_check)
        
        soup = BeautifulSoup(html_input_string, 'html.parser')

        value = soup.input['value']
        cursor.execute("SELECT COUNT(*) FROM participant WHERE username = %s", (value,))
        user = cursor.fetchone()[0]
        if user:
            pass
        else:
            raise ValidationError('Participant does not exists! Please try a different username')
        
    def validate_event_name(self, username_to_check):
         
        html_input_string = str(username_to_check)

        soup = BeautifulSoup(html_input_string, 'html.parser')

        value = soup.input['value']
        cursor.execute("SELECT COUNT(*) FROM event WHERE event_name = %s", (value,))
        user = cursor.fetchone()[0]
        if user:
            pass
        else:
            raise ValidationError('Event does not exists! Please try a different event name')
        
    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    event_name = StringField(label='Event Name',validators=[Length(min=2,max=30),DataRequired()])
    submit = SubmitField(label="Add") 
    
class RegisterGuest_HouseForm(FlaskForm):
    def validate_guest_house_name(self, username_to_check):
         
        html_input_string = str(username_to_check)
        
        soup = BeautifulSoup(html_input_string, 'html.parser')

        value = soup.input['value']
        cursor.execute("SELECT COUNT(*) FROM guest_house WHERE guest_house_name = %s", (value,))
        user = cursor.fetchone()[0]
        if user:
            raise ValidationError('Guest house name exists! Please try a different guest house name')
        
    guest_house_name = StringField(label='Guest House Name:', validators=[Length(min=2, max=30), DataRequired()])
    total_rooms = IntegerField(label='Toatl Rooms',validators=[DataRequired()])
    available_rooms = IntegerField(label='Available Rooms',validators=[DataRequired()])
    price = IntegerField(label='Tariff',validators=[DataRequired()])
    submit = SubmitField(label="Add") 


class DeleteEventForm(FlaskForm):
    submit = SubmitField(label="Delete ")
    
class RegisterEventForm(FlaskForm):
    submit = SubmitField(label="Register Event")
    
class VolunteerEventForm(FlaskForm):
    submit = SubmitField(label="Volunteer Event")
    
class AcceptVolunteerForm(FlaskForm):
    submit = SubmitField(label="Accept Volunteer")
    
class BookRoomForm(FlaskForm):
    submit = SubmitField(label="Book Room")

class ApplyVolunteerForm(FlaskForm):
    submit = SubmitField(label="Apply Volunteer")
    
class SetWinnerForm(FlaskForm):
    winner_1 = StringField(label='Winner 1:', validators=[Length(min=2, max=50), DataRequired()])
    winner_2 = StringField(label='Winner 2', validators=[Length(min=2, max=50), DataRequired()])
    winner_3 = StringField(label='Winner 3', validators=[Length(min=2, max=50), DataRequired()])
    submit = SubmitField(label="Set Winners") 
    
class FoodForm(FlaskForm):
    food_type = SelectField(label='Food Type:', choices=[('veg', 'Veg'), ('nonveg', 'Non-Veg')], validators=[DataRequired()])
    submit = SubmitField(label='Submit')



class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')


class ForgotPasswordForm_email(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    submit = SubmitField(label='Change Password')
    
class ForgotPasswordForm_username(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    submit = SubmitField(label='Submit')
    
class ForgotPasswordForm_password(FlaskForm):
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Change Password')



    

