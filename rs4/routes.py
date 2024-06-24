from rs4 import app
from flask import render_template, redirect, url_for, flash, request, session
from rs4.models import *
from rs4.forms import *
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

logged_in = False
    
@app.route('/admin', methods=['GET', 'POST'])
def admin_page():
    role = session.get('role')
    if role == 'admin':
        if 'username' in session:
            logged_in = True
            current_user = current_user_cls(session.get('username'),logged_in)
        else:
            logged_in = False
            current_user = current_user_cls(None,logged_in)
        return render_template('admin.html',current_user = current_user, role = role)
    else:
        flash("You are not allowed to access this URL",category='danger')
        return redirect(url_for('home_page'))

@app.route('/add_student', methods=['GET', 'POST'])
def add_student_page():
    role = session.get('role')
    if role == 'admin':
        form = RegisterStudentForm()
        if form.validate_on_submit():
            name = form.name.data
            roll = form.roll.data
            username = form.username.data
            dept = form.dept.data
            password = form.password1.data
            password = bcrypt.generate_password_hash(password).decode('utf-8')
            email = form.email.data
            try:
                cursor.execute("INSERT INTO student (username, password, roll, name, dept, email) VALUES (%s, %s, %s, %s, %s, %s)",
                            (username, password, roll, name, dept, email))
                connection.commit()
                flash(
                f"successfully! You have now registered {username}", category='success')

            except (Exception, psycopg2.Error) as error:
                print("Error while inserting data into PostgreSQL", error)
                flash(
                f"Error!! try again", category='danger')
            return redirect(url_for('admin_page'))
        if form.errors != {}:  
            for err_msg in form.errors.values():
                flash(
                    f'There was an error with creating a user: {err_msg}', category='danger')
        if 'username' in session:
            logged_in = True
            current_user = current_user_cls(session.get('username'),logged_in)
        else:
            logged_in = False
            current_user = current_user_cls(None,logged_in)
        return render_template('register_student.html', form=form,current_user = current_user, role = role)
    else:
        flash("You are not allowed to access this URL",category='danger')
        return redirect(url_for('home_page'))


@app.route('/add_participant', methods=['GET', 'POST'])
def add_participant_page():
    role = session.get('role')
    if role == 'admin':
        form = RegisterParticipantForm()
        if form.validate_on_submit():
            name = form.name.data
            college_name = form.college_name.data
            address = form.address.data
            contact = form.contact.data
            username = form.username.data
            password = form.password1.data
            password = bcrypt.generate_password_hash(password).decode('utf-8')
            email = form.email.data
            try:
                cursor.execute("INSERT INTO participant (username, password, name, email,college_name,address,contact) VALUES (%s,%s,%s,%s, %s, %s, %s)",
                            (username, password, name, email,college_name,address,contact))

                connection.commit()
                flash(
                f"successfully! You have now registered {username}", category='success')

            except (Exception, psycopg2.Error) as error:
                print("Error while inserting data into PostgreSQL", error)
                flash(
                f"Error!! try again", category='danger')
        
            return redirect(url_for('admin_page'))
        if form.errors != {}:  
            for err_msg in form.errors.values():
                flash(
                    f'There was an error with creating a user: {err_msg}', category='danger')
        if 'username' in session:
            logged_in = True
            current_user = current_user_cls(session.get('username'),logged_in)
        else:
            logged_in = False
            current_user = current_user_cls(None,logged_in)
        return render_template('register_participant.html', form=form,current_user = current_user, role = role)
    else:
        flash("You are not allowed to access this URL",category='danger')
        return redirect(url_for('home_page'))


@app.route('/add_organizer', methods=['GET', 'POST'])
def add_organizer_page():
    role = session.get('role')
    if role == 'admin':
        form = RegisterOrganizerForm()
        if form.validate_on_submit():
            name = form.name.data
            username = form.username.data
            password = form.password1.data
            password = bcrypt.generate_password_hash(password).decode('utf-8')
            email = form.email.data
            try:
                cursor.execute("INSERT INTO organizer (username, password, name, email) VALUES (%s,%s,%s,%s)",
                            (username, password, name, email))
                connection.commit()
                flash(
                    f"successfully! You have now registered {username}", category='success')

            except (Exception, psycopg2.Error) as error:
                print("Error while inserting data into PostgreSQL", error)
                flash(
                f"Error!! try again", category='danger')
            
            return redirect(url_for('admin_page'))
        
        if form.errors != {}:  
            for err_msg in form.errors.values():
                flash(
                    f'There was an error with creating a user: {err_msg}', category='danger')
                
        if 'username' in session:
            logged_in = True
            current_user = current_user_cls(session.get('username'),logged_in)
        else:
            logged_in = False
            current_user = current_user_cls(None,logged_in)
        return render_template('register_organizer.html', form=form, current_user = current_user, role = role)
    else:
        flash("You are not allowed to access this URL",category='danger')
        return redirect(url_for('home_page'))
    


@app.route('/add_event', methods=['GET', 'POST'])
def add_event_page():
    role = session.get('role')
    if role == 'admin':
        form = AdminCreateEventForm()
        if form.validate_on_submit():
            
            event_name= form.event_name.data
            date = form.date.data
            time = form.time.data
            description = form.description.data
            first_prize_amt = form.first_prize_amt.data
            second_prize_amt = form.second_prize_amt.data
            third_prize_amt = form.third_prize_amt.data
            org_name = form.org_name.data
            try:
                cursor.execute("INSERT INTO event (event_name,date,time ,description ,first_prize_amt ,second_prize_amt ,third_prize_amt, org_name) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                            (event_name,date,time ,description ,first_prize_amt ,second_prize_amt ,third_prize_amt,org_name))   
                connection.commit()
                flash(
                f"Event {event_name} created successfully by {session['username']}", category="success")

            except (Exception, psycopg2.Error) as error:
                print("Error while inserting data into PostgreSQL", error)
                flash(
                f"Error!! try again", category='danger')
        
            return redirect(url_for('admin_page'))
    
        if form.errors != {}:
            for err_msg in form.errors.values():
                flash(
                    f'There is was error creating an event, Try again !!:{err_msg}', category='danger')
        if 'username' in session:
            logged_in = True
            current_user = current_user_cls(session.get('username'),logged_in)
        else:
            logged_in = False
            current_user = current_user_cls(None,logged_in)
            
        role = session.get('role')
        return render_template('create_event.html', form=form, current_user = current_user, role = role)
    else:
        flash("You are not allowed to access this URL",category='danger')
        return redirect(url_for('home_page'))   

@app.route('/add_student_event', methods=['GET', 'POST'])
def add_student_event_page():
    role = session.get('role')
    if role == 'admin':
        form = RegisterStudent_EventForm()
        if form.validate_on_submit():
            username = form.username.data
            event_name = form.event_name.data
            try:
                cursor.execute("INSERT INTO student_event (username, event_name) VALUES (%s,%s)",
                            (username, event_name))
                connection.commit()
                flash(
                f"successfully! You have now registered {username} for the event {event_name}", category='success')

            except (Exception, psycopg2.Error) as error:
                print("Error while inserting data into PostgreSQL", error)
                flash(
                f"Error!! try again", category='danger')

            return redirect(url_for('admin_page'))
        
        if form.errors != {}:  
            for err_msg in form.errors.values():
                flash(
                    f'There was an error with creating a student_event: {err_msg}', category='danger')
                
        if 'username' in session:
            logged_in = True
            current_user = current_user_cls(session.get('username'),logged_in)
        else:
            logged_in = False
            current_user = current_user_cls(None,logged_in)
            
        return render_template('add_student_event.html', form=form, current_user = current_user, role = role)
    else:
        flash("You are not allowed to access this URL",category='danger')
        return redirect(url_for('home_page'))   

@app.route('/add_participant_event', methods=['GET', 'POST'])
def add_participant_event_page():
    role = session.get('role')
    if role == 'admin':
        form = RegisterParticipant_EventForm()
        if form.validate_on_submit():
            username = form.username.data
            event_name = form.event_name.data
            try:
                cursor.execute("INSERT INTO participant_event (username, event_name) VALUES (%s,%s)",
                            (username, event_name))
                
                connection.commit()
                flash(
                    f"successfully! You have now registered {username} for the event {event_name}", category='success')

            except (Exception, psycopg2.Error) as error:
                print("Error while inserting data into PostgreSQL", error)
                flash(
                f"Error!! try again", category='danger') 
            
            return redirect(url_for('admin_page'))
        
        if form.errors != {}:  
            for err_msg in form.errors.values():
                flash(
                    f'There was an error with creating a participant_event: {err_msg}', category='danger')
                
        if 'username' in session:
            logged_in = True
            current_user = current_user_cls(session.get('username'),logged_in)
        else:
            logged_in = False
            current_user = current_user_cls(None,logged_in)
            
        return render_template('add_student_event.html', form=form, current_user = current_user, role = role)
    else:
        flash("You are not allowed to access this URL",category='danger')
        return redirect(url_for('home_page'))   

@app.route('/add_volunteer_event', methods=['GET', 'POST'])
def add_volunteer_event_page():
    role = session.get('role')
    if role == 'admin':
        form = RegisterStudent_EventForm()
        if form.validate_on_submit():
            username = form.username.data
            event_name = form.event_name.data
            try:
                cursor.execute("INSERT INTO volunteer_event (username, event_name) VALUES (%s,%s)",
                            (username, event_name))

                connection.commit()
                flash(
                    f"successfully! You have now registered {username} as a volunteer for the event {event_name}", category='success')

            except (Exception, psycopg2.Error) as error:
                print("Error while inserting data into PostgreSQL", error)
                flash(
                f"Error!! try again", category='danger') 
            
            return redirect(url_for('admin_page'))
        if form.errors != {}:  
            for err_msg in form.errors.values():
                flash(
                    f'There was an error with creating a volunteer_event: {err_msg}', category='danger')
                
        if 'username' in session:
            logged_in = True
            current_user = current_user_cls(session.get('username'),logged_in)
        else:
            logged_in = False
            current_user = current_user_cls(None,logged_in)
            
        return render_template('add_student_event.html', form=form, current_user = current_user, role = role)
    else:
        flash("You are not allowed to access this URL",category='danger')
        return redirect(url_for('home_page'))   

@app.route('/add_guest_house', methods=['GET', 'POST'])
def add_guest_house_page():
    role = session.get('role')
    if role == 'admin': 
        form = RegisterGuest_HouseForm()
        if form.validate_on_submit():
            guest_house_name = form.guest_house_name.data
            total_rooms = form.total_rooms.data
            avaiable_rooms = form.available_rooms.data
            price = form.price.data
            try:
                cursor.execute("INSERT INTO guest_house (guest_house_name,total_rooms,available_rooms,price) VALUES (%s,%s,%s,%s)",
                            (guest_house_name,total_rooms,avaiable_rooms,price))

                connection.commit()
                flash(
                    f"successfully! You have now registered a guest house {guest_house_name}", category='success')

            except (Exception, psycopg2.Error) as error:
                print("Error while inserting data into PostgreSQL", error)
                flash(
                f"Error!! try again", category='danger') 
            
            return redirect(url_for('admin_page'))
        
        if form.errors != {}:  
            for err_msg in form.errors.values():
                flash(
                    f'There was an error with creating a guest house: {err_msg}', category='danger')
                
        if 'username' in session:
            logged_in = True
            current_user = current_user_cls(session.get('username'),logged_in)
        else:
            logged_in = False
            current_user = current_user_cls(None,logged_in)
            
        return render_template('add_guest_house.html', form=form, current_user = current_user, role = role)
    else:
        flash("You are not allowed to access this URL",category='danger')
        return redirect(url_for('home_page'))  

@app.route('/view_student', methods=["GET", "POST"])
def view_student_page():
    role = session.get('role')
    if role == 'admin':
        delete_event_form = DeleteEventForm()
        if request.method == "POST":
            del_event_name = request.form.get('delete_event')
            try:
                cursor.execute("delete from student where username = %s",(del_event_name,))
                connection.commit()
                flash(
                    f"Student {del_event_name} is deleted", category="success")
            except (Exception, psycopg2.Error) as error:
                flash("Student not deleted", category="danger")
                
            return redirect(url_for('view_student_page'))

        if request.method == "GET":
            try:
                cursor.execute("select * from student")
                items = cursor.fetchall()
                
                connection.commit()
                
            except (Exception, psycopg2.Error) as error:
                print("Error while extracting data from PostgreSQL", error)
                
            if 'username' in session:
                logged_in = True
                current_user = current_user_cls(session.get('username'),logged_in)
            else:
                logged_in = False
                current_user = current_user_cls(None,logged_in)
            return render_template('view_student.html', current_user = current_user, events = items, delete_event_form = delete_event_form, role = role)
    else:
        flash("You are not allowed to access this URL",category='danger')
        return redirect(url_for('home_page'))  
    
@app.route('/view_participant', methods=["GET", "POST"])
def view_participant_page():
    role = session.get('role')
    if role == 'admin':
        delete_event_form = DeleteEventForm()
        if request.method == "POST":
            del_event_name = request.form.get('delete_event')
            try:
                cursor.execute("delete from participant where username = %s",(del_event_name,))
                
                connection.commit()
                flash(
                    f"Participant {del_event_name} is deleted", category="success")
            except (Exception, psycopg2.Error) as error:
                flash("Participant not deleted", category="danger")
            return redirect(url_for('view_participant_page'))

        if request.method == "GET":
            try:
                
                cursor.execute("select * from participant")
                items = cursor.fetchall()
                
                connection.commit()
                
            except (Exception, psycopg2.Error) as error:
                print("Error while extracting data from PostgreSQL", error)
            if 'username' in session:
                logged_in = True
                current_user = current_user_cls(session.get('username'),logged_in)
            else:
                logged_in = False
                current_user = current_user_cls(None,logged_in)
            return render_template('view_participant.html', current_user = current_user, events = items, delete_event_form = delete_event_form, role = role)
    else:
        flash("You are not allowed to access this URL",category='danger')
        return redirect(url_for('home_page'))  

    
@app.route('/view_organizer', methods=["GET", "POST"])
def view_organizer_page():
    role = session.get('role')
    if role == 'admin':
        delete_event_form = DeleteEventForm()
        if request.method == "POST":
            del_event_name = request.form.get('delete_event')
            try:
                cursor.execute("delete from organizer where username = %s",(del_event_name,))
                
                connection.commit()
                flash(
                    f"Organizer {del_event_name} is deleted", category="success")
            except (Exception, psycopg2.Error) as error:
                flash("Organizer not deleted", category="danger")
            return redirect(url_for('view_organizer_page'))

        if request.method == "GET":
            try:
                
                cursor.execute("select * from organizer")
                items = cursor.fetchall()
                
                connection.commit()
                
            except (Exception, psycopg2.Error) as error:
                print("Error while extracting data from PostgreSQL", error)
            if 'username' in session:
                logged_in = True
                current_user = current_user_cls(session.get('username'),logged_in)
            else:
                logged_in = False
                current_user = current_user_cls(None,logged_in)
            return render_template('view_organizer.html', current_user = current_user, events = items, delete_event_form = delete_event_form, role = role)
    else:
        flash("You are not allowed to access this URL",category='danger')
        return redirect(url_for('home_page'))  

@app.route('/view_event', methods=["GET", "POST"])
def view_event_page():
    role = session.get('role')
    if role == 'admin':
        delete_event_form = DeleteEventForm()
        if request.method == "POST":
            del_event_name = request.form.get('delete_event')
            try:
                
                cursor.execute("delete from event where event_name = %s",(del_event_name,))
                
                connection.commit()
                flash(
                    f"Event {del_event_name} is deleted", category="success")
            except (Exception, psycopg2.Error) as error:
                flash("Event not deleted", category="danger")
            return redirect(url_for('view_event_page'))

        if request.method == "GET":
            try:
                
                cursor.execute("select * from event")
                items = cursor.fetchall()
                
                connection.commit()
                
            except (Exception, psycopg2.Error) as error:
                print("Error while extracting data from PostgreSQL", error)
            if 'username' in session:
                logged_in = True
                current_user = current_user_cls(session.get('username'),logged_in)
            else:
                logged_in = False
                current_user = current_user_cls(None,logged_in)
            return render_template('view_event.html', current_user = current_user, events = items, delete_event_form = delete_event_form, role = role)
    else:
        flash("You are not allowed to access this URL",category='danger')
        return redirect(url_for('home_page'))  

@app.route('/view_student_event', methods=["GET", "POST"])
def view_student_event_page():
    role = session.get('role')
    if role == 'admin':
        delete_event_form = DeleteEventForm()
        if request.method == "POST":
            del_event_name = request.form.get('delete_event')
            elements = del_event_name.strip('()').split(', ')
            try:
                cursor.execute("delete from student_event where event_name = %s and username=%s",(elements[1][1:-1],elements[0][1:-1]))
                
                connection.commit()

                flash(
                    f"Student_event {del_event_name} is deleted", category="success")
            except (Exception, psycopg2.Error) as error:
                flash("Student_event not deleted", category="danger")
            return redirect(url_for('view_student_event_page'))

        if request.method == "GET":
            try:
                
                cursor.execute("select * from student_event")
                items = cursor.fetchall()
                
                connection.commit()
                
            except (Exception, psycopg2.Error) as error:
                print("Error while extracting data from PostgreSQL", error)
            if 'username' in session:
                logged_in = True
                current_user = current_user_cls(session.get('username'),logged_in)
            else:
                logged_in = False
                current_user = current_user_cls(None,logged_in)
            return render_template('view_student_event.html', current_user = current_user, events = items, delete_event_form = delete_event_form, role = role)
    else:
        flash("You are not allowed to access this URL",category='danger')
        return redirect(url_for('home_page'))  

@app.route('/view_participant_event', methods=["GET", "POST"])
def view_participant_event_page():
    role = session.get('role')
    if role == 'admin':
        delete_event_form = DeleteEventForm()
        if request.method == "POST":
            del_event_name = request.form.get('delete_event')
            elements = del_event_name.strip('()').split(', ')
            try:
                cursor.execute("delete from participant_event where event_name = %s and username=%s",(elements[1][1:-1],elements[0][1:-1]))
                
                connection.commit()

                flash(
                    f"Participant_Event {del_event_name} is deleted", category="success")
            except (Exception, psycopg2.Error) as error:
                flash("Participant_Event not deleted", category="danger")
            return redirect(url_for('view_participant_event_page'))

        if request.method == "GET":
            try:
                
                cursor.execute("select * from participant_event")
                items = cursor.fetchall()
                
                connection.commit()
                
            except (Exception, psycopg2.Error) as error:
                print("Error while extracting data from PostgreSQL", error)
            if 'username' in session:
                logged_in = True
                current_user = current_user_cls(session.get('username'),logged_in)
            else:
                logged_in = False
                current_user = current_user_cls(None,logged_in)
            return render_template('view_student_event.html', current_user = current_user, events = items, delete_event_form = delete_event_form, role = role)
    else:
        flash("You are not allowed to access this URL",category='danger')
        return redirect(url_for('home_page'))  

@app.route('/view_volunteer_event', methods=["GET", "POST"])
def view_volunteer_event_page():
    role = session.get('role')
    if role == 'admin':
        delete_event_form = DeleteEventForm()
        if request.method == "POST":
            del_event_name = request.form.get('delete_event')
            elements = del_event_name.strip('()').split(', ')
            try:
                cursor.execute("delete from volunteer_event where event_name = %s and username=%s",(elements[1][1:-1],elements[0][1:-1]))
                
                connection.commit()

                flash(
                    f"Volunteer_Event {del_event_name} is deleted", category="success")
            except (Exception, psycopg2.Error) as error:
                flash("Volunteer_Event not deleted", category="danger")
            return redirect(url_for('view_volunteer_event_page'))

        if request.method == "GET":
            try:
                
                cursor.execute("select * from volunteer_event")
                items = cursor.fetchall()
                
                connection.commit()
                
            except (Exception, psycopg2.Error) as error:
                print("Error while extracting data from PostgreSQL", error)
            if 'username' in session:
                logged_in = True
                current_user = current_user_cls(session.get('username'),logged_in)
            else:
                logged_in = False
                current_user = current_user_cls(None,logged_in)
            return render_template('view_student_event.html', current_user = current_user, events = items, delete_event_form = delete_event_form, role = role)
    else:
        flash("You are not allowed to access this URL",category='danger')
        return redirect(url_for('home_page'))  

@app.route('/view_guest_house', methods=["GET", "POST"])
def view_guest_house_page():
    role = session.get('role')
    if role == 'admin':
        delete_event_form = DeleteEventForm()
        if request.method == "POST":
            del_event_name = request.form.get('delete_event')
            try:
                cursor.execute("delete from guest_house where guest_house_name = %s ",(del_event_name,))
                
                connection.commit()

                flash(
                    f"Guest House {del_event_name} is deleted", category="success")
            except (Exception, psycopg2.Error) as error:
                flash("Guest House not deleted", category="danger")
            return redirect(url_for('view_guest_house_page'))

        if request.method == "GET":
            try:
                
                cursor.execute("select * from guest_house")
                items = cursor.fetchall()
                
                connection.commit()
                
            except (Exception, psycopg2.Error) as error:
                print("Error while extracting data from PostgreSQL", error)
            if 'username' in session:
                logged_in = True
                current_user = current_user_cls(session.get('username'),logged_in)
            else:
                logged_in = False
                current_user = current_user_cls(None,logged_in)
            return render_template('view_guest_house.html', current_user = current_user, events = items, delete_event_form = delete_event_form, role = role)
    else:
        flash("You are not allowed to access this URL",category='danger')
        return redirect(url_for('home_page'))  



@app.route('/')
@app.route('/home')
def home_page(): 
    if 'username' in session:
        logged_in = True
        current_user = current_user_cls(session.get('username'),logged_in)
    else:
        logged_in = False
        current_user = current_user_cls(None,logged_in)
        
    return render_template('home.html',current_user = current_user)



@app.route('/contact_us') 
def contact_us_page():
    if 'username' in session:
        logged_in = True
        current_user = current_user_cls(session.get('username'),logged_in)
    else:
        logged_in = False
        current_user = current_user_cls(None,logged_in)
    return render_template('contact_us.html',current_user = current_user)


@app.route('/organizer')
def organizer_page():
    userrole = session.get('role')
    if userrole == "organizer": 
        if 'username' in session:
            logged_in = True
            current_user = current_user_cls(session.get('username'),logged_in)
        else:
            logged_in = False
            current_user = current_user_cls(None,logged_in)
        return render_template('organizer.html',current_user = current_user, role=userrole)
    else:
        return redirect(url_for("login_page"))



@app.route('/dashboard')
def dashboard_page():
    userrole = session.get('role')
    if userrole == "student":
        return redirect(url_for('student_page'))
    elif userrole == "participant":
        return redirect(url_for('participant_page'))
    elif userrole == "organizer":
        return redirect(url_for('organizer_page'))
    elif userrole == "admin":
        return redirect(url_for('admin_page'))
    else:
        return redirect(url_for('home_page'))
        
        
@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if 'username' in session:
        logged_in = True
        current_user = current_user_cls(session.get('username'),logged_in)
    else:
        logged_in = False
        current_user = current_user_cls(None,logged_in)
    return render_template('register.html',current_user = current_user)


@app.route('/register_student', methods=['GET', 'POST'])
def register_student_page():
    form = RegisterStudentForm()
    if form.validate_on_submit():
        name = form.name.data
        roll = form.roll.data
        username = form.username.data
        dept = form.dept.data
        password = form.password1.data
        password = bcrypt.generate_password_hash(password).decode('utf-8')
        email = form.email.data
        try:
            cursor.execute("INSERT INTO student (username, password, roll, name, dept, email) VALUES (%s, %s, %s, %s, %s, %s)",
                        (username, password, roll, name, dept, email))

            
            connection.commit()
            flash(
                f"successfully! You are now registered in as {username}", category='success')

        except (Exception, psycopg2.Error) as error:
            print("Error while inserting data into PostgreSQL", error)
            flash(
            f"Error!! try again", category='danger') 
        
        return redirect(url_for('login_page'))
    
    if form.errors != {}:  
        for err_msg in form.errors.values():
            flash(
                f'There was an error with creating a user: {err_msg}', category='danger')
    if 'username' in session:
        logged_in = True
        current_user = current_user_cls(session.get('username'),logged_in)
    else:
        logged_in = False
        current_user = current_user_cls(None,logged_in)
    return render_template('register_student.html', form=form,current_user = current_user)


@app.route('/register_participant', methods=['GET', 'POST'])
def register_participant_page():
    form = RegisterParticipantForm()
    if form.validate_on_submit():
        name = form.name.data
        college_name = form.college_name.data
        address = form.address.data
        contact = form.contact.data
        username = form.username.data
        password = form.password1.data
        password = bcrypt.generate_password_hash(password).decode('utf-8')
        email = form.email.data
        try:            
            cursor.execute("INSERT INTO participant (username, password, name, email,college_name,address,contact) VALUES (%s,%s,%s,%s, %s, %s, %s)",
                        (username, password, name, email,college_name,address,contact))

            
            connection.commit()
            flash(
                f"successfully! You are now registered in as {username}", category='success')

        except (Exception, psycopg2.Error) as error:
            print("Error while inserting data into PostgreSQL", error)
            flash(
            f"Error!! try again", category='danger') 
        
        return redirect(url_for('login_page'))
    
    if form.errors != {}:  
        for err_msg in form.errors.values():
            flash(
                f'There was an error with creating a user: {err_msg}', category='danger')
    if 'username' in session:
        logged_in = True
        current_user = current_user_cls(session.get('username'),logged_in)
    else:
        logged_in = False
        current_user = current_user_cls(None,logged_in)
    return render_template('register_participant.html', form=form,current_user = current_user)

@app.route('/register_organizer', methods=['GET', 'POST'])
def register_organizer_page():
    form = RegisterOrganizerForm()
    if form.validate_on_submit():
        name = form.name.data
        username = form.username.data
        password = form.password1.data
        password = bcrypt.generate_password_hash(password).decode('utf-8')
        email = form.email.data
        try:
            cursor.execute("INSERT INTO organizer (username, password, name, email) VALUES (%s,%s,%s,%s)",
                        (username, password, name, email))

            
            connection.commit()

            flash(
                f"successfully! You are now registered in as {username}", category='success')

        except (Exception, psycopg2.Error) as error:
            print("Error while inserting data into PostgreSQL", error)
            flash(
            f"Error!! try again", category='danger') 
        
        return redirect(url_for('login_page'))
    
    if form.errors != {}:  
        for err_msg in form.errors.values():
            flash(
                f'There was an error with creating a user: {err_msg}', category='danger')
    if 'username' in session:
        logged_in = True
        current_user = current_user_cls(session.get('username'),logged_in)
    else:
        logged_in = False
        current_user = current_user_cls(None,logged_in)
    return render_template('register_organizer.html', form=form, current_user = current_user)




@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if 'username' in session:
        logged_in = True
        current_user = current_user_cls(session.get('username'),logged_in)
    else:
        logged_in = False
        current_user = current_user_cls(None,logged_in)
    return render_template('login.html', current_user = current_user)


@app.route('/login_student', methods=['GET', 'POST'])
def login_student_page():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if(authenticate(username,password,"student")):
            session['username'] = username
            session['role'] = 'student'
            flash(
                f"You are logged in as: {username}", category='success')
            return redirect(url_for('student_page'))
        else:
            flash("Please try again", category='danger')
            
    if form.errors != {}:  
        for err_msg in form.errors.values():
            flash(
                f'There was an error with logging in user: {err_msg}', category='danger')
    if 'username' in session:
        logged_in = True
        current_user = current_user_cls(session.get('username'),logged_in)
    else:
        logged_in = False
        current_user = current_user_cls(None,logged_in)
    return render_template('login_form.html', form=form, current_user = current_user, role = 'student')     

@app.route('/login_participant', methods=['GET', 'POST'])
def login_participant_page():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if(authenticate(username,password,"participant")):
            session['username'] = username
            session['role'] = 'participant'
            flash(
                f"You are logged in as: {username}", category='success')
            return redirect(url_for('participant_page'))
        else:
            flash("Please try again", category='danger')
            
    if form.errors != {}:  
        for err_msg in form.errors.values():
            flash(
                f'There was an error with logging in user: {err_msg}', category='danger', role = 'participant')
            
    if 'username' in session:
        logged_in = True
        current_user = current_user_cls(session.get('username'),logged_in)
    else:
        logged_in = False
        current_user = current_user_cls(None,logged_in)
    return render_template('login_form.html', form=form, current_user = current_user)  

@app.route('/login_organizer', methods=['GET', 'POST'])
def login_organizer_page():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if(authenticate(username,password,"organizer")):
            session['username'] = username
            session['role'] = 'organizer'
            flash(
                f"You are logged in as: {username}", category='success')
            return redirect(url_for('organizer_page'))
        else:
            flash("Please try again", category='danger')
            
    if form.errors != {}:  
        for err_msg in form.errors.values():
            flash(
                f'There was an error with logging in user: {err_msg}', category='danger', role = 'organizer')
            
    if 'username' in session:
        logged_in = True
        current_user = current_user_cls(session.get('username'),logged_in)
    else:
        logged_in = False
        current_user = current_user_cls(None,logged_in)
    return render_template('login_form.html', form=form, current_user = current_user)  

@app.route('/login_admin', methods=['GET', 'POST'])
def login_admin_page():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if(authenticate(username,password,"admin")):
            session['username'] = username
            session['role'] = 'admin'
            flash(
                f"You are logged in as: {username}", category='success')
            return redirect(url_for('admin_page'))
        else:
            flash("Please try again", category='danger')
    if form.errors != {}:  
        for err_msg in form.errors.values():
            flash(
                f'There was an error with logging in user: {err_msg}', category='danger')
            
    if 'username' in session:
        logged_in = True
        current_user = current_user_cls(session.get('username'),logged_in)
    else:
        logged_in = False
        current_user = current_user_cls(None,logged_in)
    return render_template('login_form.html', form=form, current_user = current_user, role = 'admin') 
    
@app.route('/logout')
def logout_page():
    session.pop('username', None)
    session.pop('role',None)
    return redirect(url_for("home_page"))

# forget_username = None
# @app.route('/forget_password/<token>', methods=['GET', 'POST'])
# def forget_password_page(token):
#     # token = token[1:-1]
#     form = ForgotPasswordForm_username()
#     username = None
#     if form.validate_on_submit:
#         username = form.username.data
#         if username is not None:
#             forget_username = username
#         if token == 'student':
#             cursor.execute("select count(*) from student where username = %s",(username,))
#         elif token == 'participant':
#             cursor.execute("select count(*) from participant where username = %s",(username,))
#         elif token == 'organizer':
#             cursor.execute("select count(*) from organizer where username = %s",(username,))
        
#         num = cursor.fetchall()[0]
#         if num == 0:
#             flash("Username does not exist", category='danger')
#             return redirect(url_for('login_page'))

#     form1 = ForgotPasswordForm_email()
#     form2 = ForgotPasswordForm_password()
#     if form2.validate_on_submit():
#         password = form2.password.data
#         password = bcrypt.generate_password_hash(password).decode('utf-8')
#         try:
#             if token == 'student':
#                 cursor.execute("update student set password = %s where username = %s",(password,forget_username))
#             elif token == 'participant':
#                 cursor.execute("update participant set password = %s where username = %s",(password,forget_username))
#             elif token == 'organizer':
#                 cursor.execute("update organizer set password = %s where username = %s",(password,forget_username))
#             connection.commit()
#         except:
#             print("error!!")
    
            
        
#         flash(
#             f"password changed succesfully", category='success')
#         return redirect(url_for('login_page'))
#     else:
#         # flash("Please try again", category='danger')
#         pass
#     if 'username' in session:
#         logged_in = True
#         current_user = current_user_cls(session.get('username'),logged_in)
#     else:
#         logged_in = False
#         current_user = current_user_cls(None,logged_in)
#     return render_template('forget_password.html', form2=form2, form1=form1, current_user = current_user, form = form)


@app.route('/create_event', methods=['GET', 'POST'])
def create_event_page():
    role = session.get('role')
    if role == 'organizer':
        form = CreateEventForm()
        if form.validate_on_submit():
            event_name= form.event_name.data
            date = form.date.data
            time = form.time.data
            description = form.description.data
            first_prize_amt = form.first_prize_amt.data
            second_prize_amt = form.second_prize_amt.data
            third_prize_amt = form.third_prize_amt.data
            try:
                cursor.execute("INSERT INTO event (event_name,date,time ,description ,first_prize_amt ,second_prize_amt ,third_prize_amt,org_name) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                            (event_name,date,time ,description ,first_prize_amt ,second_prize_amt ,third_prize_amt,session.get('username')))

                connection.commit()
                flash(
                    f"Event {event_name} created successfully by {session['username']}", category="success")

            except (Exception, psycopg2.Error) as error:
                print("Error while inserting data into PostgreSQL", error)
                flash("Error!! Try again")
            
            return redirect(url_for('organizer_page'))
        
        if form.errors != {}:
            for err_msg in form.errors.values():
                flash(
                    f'There is was error creating an event, Try again !!:{err_msg}', category='danger')
        if 'username' in session:
            logged_in = True
            current_user = current_user_cls(session.get('username'),logged_in)
        else:
            logged_in = False
            current_user = current_user_cls(None,logged_in)
        return render_template('create_event.html', form=form, current_user = current_user)
    else:
        flash("You are not allowed to access this URL",category="danger")
        return redirect(url_for('dashboard_page'))

@app.route('/organizer_events', methods=["GET", "POST"])
def organizer_events_page():
    role = session.get('role')
    if role == 'organizer':
        delete_event_form = DeleteEventForm()
        if request.method == "POST":
            del_event_name = request.form.get('delete_event')
            try:    
                cursor.execute("delete from event where event_name = %s",(del_event_name,))
                
                connection.commit()
                flash(
                    f"Event {del_event_name} is deleted", category="success")
            except (Exception, psycopg2.Error) as error:
                flash("Event not deleted", category="danger")
            return redirect(url_for('organizer_events_page'))

        if request.method == "GET":
            try:
                
                cursor.execute("select * from event where org_name = %s",(session.get('username'),))
                items = cursor.fetchall()
                
                connection.commit()
                
            except (Exception, psycopg2.Error) as error:
                print("Error while extracting data from PostgreSQL", error)
            if 'username' in session:
                logged_in = True
                current_user = current_user_cls(session.get('username'),logged_in)
            else:
                logged_in = False
                current_user = current_user_cls(None,logged_in)
            return render_template('organizer_events.html', current_user = current_user, events = items, delete_event_form = delete_event_form)
    else:
        flash("You are not allowed to access this URL",category="danger")
        return redirect(url_for('dashboard_page'))
    
    
@app.route('/event_details/<token>', methods=["GET", "POST"])
def event_details_page(token):
    accept_volunteer_form = AcceptVolunteerForm()
    role = session.get('role')
    username = session.get('username')
    num = 1
    if role == 'organizer':
        cursor.execute("select count(*) from event where event_name = %s and org_name = %s",(token,username))
        num = cursor.fetchall()[0][0]
        num = num
    
    if role is not None and num == 1:
        if request.method == "POST":
            accept_volunteer = request.form.get('accept_volunteer')
            try: 
                cursor.execute("update volunteer_event set status = 'sanctioned' where username = %s and event_name = %s",(accept_volunteer,token))
                
                connection.commit()
                flash(
                    f"Volunteer {accept_volunteer}'s application is accepted", category="success")
            except (Exception, psycopg2.Error) as error:
                flash("Volunteer not accepted", category="danger")
            return redirect(url_for('event_details_page',token = token))
            
        
        if request.method == "GET":
            try:
                cursor.execute("select * from event where event_name = %s",(token,))
                event = cursor.fetchall()
                cursor.execute("select * from student where username in (select username from volunteer_event where event_name = %s and status = 'pending')",(token,))
                pending_volunteers = cursor.fetchall()
                cursor.execute("select * from student where username in (select username from volunteer_event where event_name = %s and status = 'sanctioned')",(token,))
                sanctioned_volunteers = cursor.fetchall()
                
            except (Exception, psycopg2.Error) as error:
                print("Error while inserting data into PostgreSQL ************", error)
            
            if 'username' in session:
                logged_in = True
                current_user = current_user_cls(session.get('username'),logged_in)
            else:
                logged_in = False
                current_user = current_user_cls(None,logged_in)
            role = session.get('role')
            
            return render_template('event_details.html', current_user = current_user, event = event[0], pending_volunteers = pending_volunteers,sanctioned_volunteers = sanctioned_volunteers, role = role, accept_volunteer_form = accept_volunteer_form)
    else:
        flash("You are not allowed to access this URL",category="danger")
        return redirect(url_for('dashboard_page'))
    
@app.route('/set_winners/<token>', methods=['GET', 'POST'])
def set_winners_page(token):
    role = session.get('role')
    username = session.get('username')
    cursor.execute("select count(*) from event where event_name = %s and org_name = %s",(token,username))
    num = cursor.fetchall()[0]
    if role == 'organizer' and num[0] != 0:
        form = SetWinnerForm()
        if form.validate_on_submit():
            winner1 = form.winner_1.data
            winner2 = form.winner_2.data
            winner3 = form.winner_3.data
            try:
                cursor.execute("(select * from student_event where username = %s and event_name = %s) union (select * from participant_event where username = %s and event_name = %s)",(winner1,token,winner1,token))
                len1 = len(cursor.fetchall())
                cursor.execute("(select * from student_event where username = %s and event_name = %s) union (select * from participant_event where username = %s and event_name = %s)",(winner2,token,winner2,token))
                len2 = len(cursor.fetchall())
                cursor.execute("(select * from student_event where username = %s and event_name = %s) union (select * from participant_event where username = %s and event_name = %s)",(winner3,token,winner3,token))
                len3 = len(cursor.fetchall())
                if len1 == 0 or len2 == 0 or len3 == 0:
                    flash(
                        f"Winners not participated in {token}", category='danger')
                    return redirect(url_for('event_details_page'))
                else:
                    cursor.execute("UPDATE event SET winner_1 = %s, winner_2 = %s, winner_3 =  %s WHERE event_name = %s;",(winner1,winner2,winner3,token))

                    connection.commit()
                    print("Record inserted successfully")
                    flash(
                        f"Event {token} winners set successfully", category='success')
                    return redirect(url_for('event_details_page', token = token))

            except (Exception, psycopg2.Error) as error:
                print("Error while inserting data into PostgreSQL", error)
                    
        if form.errors != {}:
            for err_msg in form.errors.values():
                flash(
                    f'There is was error setting winners, Try again !!:{err_msg}', category='danger')
                
        if 'username' in session:
            logged_in = True
            current_user = current_user_cls(session.get('username'),logged_in)
        else:
            logged_in = False
            current_user = current_user_cls(None,logged_in)
        return render_template('set_winners.html', form=form,current_user = current_user)
    else:
        flash("You are not allowed to access this URL",category="danger")
        return redirect(url_for('dashboard_page'))

@app.route('/participant', methods=["GET", "POST"])
def participant_page():
    role = session.get('role')
    if role == 'participant':
        register_event_form = RegisterEventForm()
        if request.method == "POST":
            reg_event_name = request.form.get('register_event')
            try:
                cursor.execute("insert into participant_event(username,event_name) values (%s,%s)",(session.get('username'),reg_event_name))
                
                connection.commit()
                flash(
                    f"You have been successfully register for the event {reg_event_name}!!", category="success")
            except (Exception, psycopg2.Error) as error:
                flash("You have not been registered", category="danger")
            return redirect(url_for('participant_page'))

        if request.method == "GET":
            registered_events = []
            nonregistered_events = []
            
            try:
                cursor.execute("select * from event where event_name in (select event_name from participant_event where username = %s)",(session.get('username'),))
                registered_events = cursor.fetchall()

                cursor.execute("select * from event where event_name not in (select event_name from participant_event where username = %s)",(session.get('username'),))
                nonregistered_events = cursor.fetchall()
                print("Extracted data successsfully")
            
            except (Exception, psycopg2.Error) as error:
                    print("Error while inserting data into PostgreSQL", error)
                

            if 'username' in session:
                logged_in = True
                current_user = current_user_cls(session.get('username'),logged_in)
            else:
                logged_in = False
                current_user = current_user_cls(None,logged_in)
            
            
            return render_template('participant.html', current_user = current_user, registered_events = registered_events, nonregistered_events = nonregistered_events, register_event_form = register_event_form)   
    else:
        flash("You are not allowed to access this URL",category="danger")
        return redirect(url_for('dashboard_page'))


@app.route('/student', methods=["GET", "POST"])
def student_page():
    role = session.get('role')
    if role == 'student':
        register_event_form = RegisterEventForm()
        volunteer_event_form = VolunteerEventForm()
        if request.method == "POST":
            reg_event_name = request.form.get('register_event')
            vol_event_name = request.form.get('volunteer_event')  
            try:
                
                if reg_event_name is not None:
                    cursor.execute("insert into student_event(username,event_name) values (%s,%s)",(session.get('username'),reg_event_name))
                    connection.commit()
                    flash(
                    f"You have been successfully registered for the event {reg_event_name}!!", category="success")
                else:
                    cursor.execute("insert into volunteer_event(username,event_name,status) values (%s,%s,%s)",(session.get('username'),vol_event_name,'pending'))
                    connection.commit()
                    flash(
                    f"You have been successfully applied for volunteering the event {vol_event_name}!!", category="success")
                
            except (Exception, psycopg2.Error) as error:
                flash("You have not been registered", category="danger")
            return redirect(url_for('student_page'))
        
        if request.method == "GET":
            registered_events = []
            idle_events = []
            
            try:        
                cursor.execute("select * from event where event_name in (select event_name from student_event where username = %s)",(session.get('username'),))
                registered_events = cursor.fetchall()
                cursor.execute("select * from event where event_name in (select event_name from volunteer_event where username = %s and status = 'pending')",(session.get('username'),))
                pending_volunteer_events = cursor.fetchall()
                cursor.execute("select * from event where event_name in (select event_name from volunteer_event where username = %s and status = 'sanctioned')",(session.get('username'),))
                sanctioned_volunteer_events = cursor.fetchall()

                cursor.execute("select * from event where event_name not in ((select event_name from student_event where username = %s) union (select event_name from volunteer_event where username = %s))",(session.get('username'),session.get('username')))
                idle_events = cursor.fetchall()
            
            
            except (Exception, psycopg2.Error) as error:
                print("Error while performing query",error)

            if 'username' in session:
                logged_in = True
                current_user = current_user_cls(session.get('username'),logged_in)
            else:
                logged_in = False
                current_user = current_user_cls(None,logged_in)
            
            
            return render_template('student.html', current_user = current_user, registered_events = registered_events, pending_volunteer_events = pending_volunteer_events, sanctioned_volunteer_events = sanctioned_volunteer_events, idle_events = idle_events ,register_event_form = register_event_form, volunteer_event_form = volunteer_event_form)
    else:
        flash("You are not allowed to access this URL",category="danger")
        return redirect(url_for('dashboard_page'))


@app.route('/profile', methods=["GET", "POST"])
def profile_page():
    role = session.get('role')
    if role is not None and role != 'admin':
        food_form = FoodForm()
        if food_form.validate_on_submit():
            food = food_form.food_type.data
            try:
                cursor.execute("UPDATE participant SET food = %s WHERE username = %s;",(food,session.get('username')))
                connection.commit()
                print("Record inserted successfully")
                flash(
                    f"Food set successfully", category='success')

            except (Exception, psycopg2.Error) as error:
                print("Error while inserting data into PostgreSQL", error)
                flash(
                    f"Food not set", category='danger')
            
            return redirect(url_for('profile_page'))
        
        if food_form.errors != {}:  
            for err_msg in food_form.errors.values():
                flash(
                    f'There was an error with setting food {err_msg}', category='danger')

        user = None
        role = session.get('role')
        guest_house = None
        if session.get('role') == 'student':
            cursor.execute("select * from student where username = %s;",(session.get('username'),))
            user = cursor.fetchall()[0]
        elif session.get('role') == 'participant':
            cursor.execute("select * from participant where username = %s;",(session.get('username'),))
            user = cursor.fetchall()[0]
            cursor.execute("select * from guest_house where guest_house_name in (select accomodation from participant where username = %s);",(session.get('username'),))
            guest_houses = cursor.fetchall()
            if len(guest_houses) > 0:
                guest_house = guest_houses[0]
                print(guest_house)
        else:
            cursor.execute("select * from organizer where username = %s;",(session.get('username'),))
            user = cursor.fetchall()[0]
            
            
        if 'username' in session:
            logged_in = True
            current_user = current_user_cls(session.get('username'),logged_in)
        else:
            logged_in = False
            current_user = current_user_cls(None,logged_in)
        return render_template('profile.html', current_user = current_user, role = role, user = user, food_form = food_form, guest_house = guest_house)
    else:
        flash("You are not allowed to access this URL",category="danger")
        return redirect(url_for('dashboard_page'))


@app.route('/guest_house', methods=["GET", "POST"])
def guest_house_page():
    role = session.get('role')
    username = session.get('username')
    cursor.execute("select count(*) from participant where username = %s and accomodation is null",(username,))
    num = cursor.fetchall()[0][0]
    if role == 'participant' and num != 0:
        book_room_form = BookRoomForm()
        if request.method == "POST":
            guest_house_name = request.form.get('book_room')
            try:
                cursor.execute("update participant set accomodation = %s where username = %s",(guest_house_name,session.get('username')))
                connection.commit()
                cursor.execute("UPDATE guest_house SET available_rooms = available_rooms - 1 WHERE guest_house_name = %s",(guest_house_name,))
                connection.commit()
                flash(f"Guest house {guest_house_name} booked successfully, enjoy your stay", category="success")
                
                
            except (Exception, psycopg2.Error) as error:
                flash("Guest house not booked", category="danger")
            return redirect(url_for('profile_page'))
        if request.method == "GET":
            try:     
                cursor.execute("select * from guest_house where available_rooms > 0")
                guest_houses = cursor.fetchall()
            except (Exception, psycopg2.Error) as error:
                print("Error while inserting data into PostgreSQL", error)
            
            if 'username' in session:
                logged_in = True
                current_user = current_user_cls(session.get('username'),logged_in)
            else:
                logged_in = False
                current_user = current_user_cls(None,logged_in)
            return render_template('guest_house.html', current_user = current_user, guest_houses = guest_houses, book_room_form = book_room_form)
    else:
        flash("You are not allowed to access this URL",category="danger")
        return redirect(url_for('dashboard_page'))
    
    
@app.route('/edit_profile_student', methods=["GET", "POST"])
def edit_profile_student_page():
    form = EditStudentForm()
    role = session.get('role')
    username = session.get('username')
    if role == 'student':
        cursor.execute("select * from student where username = %s",(username,))
        user = cursor.fetchall()[0]
        email = user[5]
        if form.validate_on_submit():
            flag = True
            name = form.name.data
            new_email = form.email.data
            
            if new_email != email:
                cursor.execute("select count(*) from student where email = %s",(new_email,))
                num = cursor.fetchall()[0][0]
                if num > 0:
                    flag = False
                    flash(f"Email {new_email} already exists!! Choose another email.", category="danger")
                    flag = flag
                    
            if flag == True:
                cursor.execute("update student set name = %s, email = %s where username = %s",(name,new_email,username))
                connection.commit()
                flash("Profile Updated", category='success')
            
            return redirect(url_for('profile_page'))
        
        if form.errors != {}:  
            for err_msg in form.errors.values():
                flash(
                    f'There was an error with updating your profile: {err_msg}', category='danger')
        
        if 'username' in session:
            logged_in = True
            current_user = current_user_cls(session.get('username'),logged_in)
        else:
            logged_in = False
            current_user = current_user_cls(None,logged_in)
            
        return render_template('edit_profile_student.html', form=form, current_user = current_user, user=user)
    else:
        flash("You are not allowed to access this URL",category="danger")
        return redirect(url_for('dashboard_page'))

@app.route('/edit_profile_participant', methods=["GET", "POST"])
def edit_profile_participant_page():
    form = EditParticipantForm()
    role = session.get('role')
    username = session.get('username')
    if role == 'participant':
        cursor.execute("select * from participant where username = %s",(username,))
        user = cursor.fetchall()[0]
        email = user[6]
        if form.validate_on_submit():
            flag = True
            name = form.name.data
            new_email = form.email.data
            college_name = form.college_name.data
            address = form.address.data
            contact = form.contact.data
            
            if new_email != email:
                cursor.execute("select count(*) from participant where email = %s",(new_email,))
                num = cursor.fetchall()[0][0]
                if num > 0:
                    flag = False
                    flash(f"Email {new_email} already exists!! Choose another email.", category="danger")
                    flag = flag
                    
            if flag == True:
                cursor.execute("update participant set name = %s, email = %s, college_name = %s, address = %s, contact = %s where username = %s",(name,new_email,college_name,address,contact,username))
                connection.commit()
                flash("Profile Updated", category='success')
            
            return redirect(url_for('profile_page'))
        
        if form.errors != {}:  
            for err_msg in form.errors.values():
                flash(
                    f'There was an error with updating your profile: {err_msg}', category='danger')
        
        if 'username' in session:
            logged_in = True
            current_user = current_user_cls(session.get('username'),logged_in)
        else:
            logged_in = False
            current_user = current_user_cls(None,logged_in)
            
        return render_template('edit_profile_participant.html', form=form, current_user = current_user, user=user)
    else:
        flash("You are not allowed to access this URL",category="danger")
        return redirect(url_for('dashboard_page'))

@app.route('/edit_profile_organizer', methods=["GET", "POST"])
def edit_profile_organizer_page():
    form = EditOrganizerForm()
    role = session.get('role')
    username = session.get('username')
    if role == 'organizer':
        cursor.execute("select * from organizer where username = %s",(username,))
        user = cursor.fetchall()[0]
        email = user[3]
        if form.validate_on_submit():
            flag = True
            name = form.name.data
            new_email = form.email.data
            
            if new_email != email:
                cursor.execute("select count(*) from organizer where email = %s",(new_email,))
                num = cursor.fetchall()[0][0]
                if num > 0:
                    flag = False
                    flash(f"Email {new_email} already exists!! Choose another email.", category="danger")
                    flag = flag
                    
            if flag == True:
                cursor.execute("update organizer set name = %s, email = %s where username = %s",(name,new_email,username))
                connection.commit()
                flash("Profile Updated", category='success')
            
            return redirect(url_for('profile_page'))
        
        if form.errors != {}:  
            for err_msg in form.errors.values():
                flash(
                    f'There was an error with updating your profile: {err_msg}', category='danger')
        
        if 'username' in session:
            logged_in = True
            current_user = current_user_cls(session.get('username'),logged_in)
        else:
            logged_in = False
            current_user = current_user_cls(None,logged_in)
            
        return render_template('edit_profile_organizer.html', form=form, current_user = current_user, user=user)
    else:
        flash("You are not allowed to access this URL",category="danger")
        return redirect(url_for('dashboard_page'))
