import psycopg2
from prettytable import PrettyTable
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

# SELECT 'DROP TABLE IF EXISTS "' || tablename || '" CASCADE;' AS sql
# FROM pg_tables
# WHERE schemaname = 'public';

#-------------------------------- CONNECTION TO DATABASE ----------------------------------
db_config = {
    'host': '127.0.0.1',
    'port': 5432,
    'user': 'postgres',
    'password': '2020',
    'database': 'postgres',
}

# Connect to the PostgreSQL database
connection = psycopg2.connect(**db_config)
cursor = connection.cursor()

#-------------------------------- CREATE TABLES IN DATABASE ----------------------------------
def run_query(query, parameters=None):
    if parameters:
        cursor.execute(query, parameters)
    else:
        cursor.execute(query)
    connection.commit()

def print_query_output(output, attributes):
    table = PrettyTable()
    table.field_names = attributes
    for row in output:
        table.add_row(row)
    print("\nQuery Output:")
    print(table)


def create_tables():

    # student table
    query = """
    CREATE TABLE student
    (
        username VARCHAR(50) PRIMARY KEY,
        password VARCHAR(100),
        roll CHAR(9),
        name VARCHAR(100),
        dept VARCHAR(50),
        email VARCHAR(100)
    );
    """
    run_query(query)

    # organizer table
    query = """
    CREATE TABLE organizer
    (
        username VARCHAR(50) PRIMARY KEY,
        password VARCHAR(100),
        name VARCHAR(100),
        email VARCHAR(100)
    );
    """
    run_query(query)

    # particiapant table
    query = """
    CREATE TABLE participant
    (
        username VARCHAR(50) PRIMARY KEY,
        password VARCHAR(100),
        name VARCHAR(100),
        college_name VARCHAR(100),
        address VARCHAR(100),
        contact char(10),
        email VARCHAR(100),
        food VARCHAR(100),
        accomodation VARCHAR(100)
    );
    """
    run_query(query)

    # event table
    query = """
    CREATE TABLE event
    (
        event_name VARCHAR(50) PRIMARY KEY,
        date DATE,
        time TIME,
        description VARCHAR(1024),
        first_prize_amt MONEY,
        second_prize_amt MONEY,
        third_prize_amt MONEY,
        winner_1 VARCHAR(50),
        winner_2 VARCHAR(50),
        winner_3 VARCHAR(50),
        org_name varchar(50),
        foreign key (org_name) references organizer(username) on delete cascade on update cascade
    );
    """
    run_query(query)

    # register_event table
    query = """
    CREATE TABLE student_event
    (
        username VARCHAR(50),
        event_name VARCHAR(50),
        foreign key (event_name) REFERENCES event(event_name) on delete cascade,
        foreign key (username) REFERENCES student(username) on delete cascade on update cascade,
        PRIMARY KEY (username, event_name)
    );
    """
    run_query(query)

    query = """
    CREATE TABLE participant_event
    (
        username VARCHAR(50),
        event_name VARCHAR(50),
        foreign key (event_name) REFERENCES event(event_name) on delete cascade,
        foreign key (username) REFERENCES participant(username) on delete cascade on update cascade,
        PRIMARY KEY (username, event_name)
    );
    """
    run_query(query)

    # volunteer_event table
    query = """
    CREATE TABLE volunteer_event
    (
        username VARCHAR(50),
        event_name VARCHAR(50),
        status VARCHAR(20),
        foreign key (event_name) REFERENCES event(event_name) on delete cascade,
        foreign key (username) REFERENCES student(username) on delete cascade on update cascade,
        PRIMARY KEY (username, event_name)
    );
    """
    run_query(query)

    query = """
    CREATE TABLE admin
    (
        username VARCHAR(50) primary key,
        password VARCHAR(100)
    );

    """
    run_query(query)

    query = """
    CREATE TABLE guest_house
    (
        guest_house_name VARCHAR(100) primary key,
        total_rooms INTEGER,
        available_rooms INTEGER,
        price MONEY
    );
    insert into guest_house values('TGH Deluxe Room',50,50,5000);
    insert into guest_house values('TGH Super Deluxe Room',50,50,10000);
    insert into guest_house values('SAM Deluxe Room',50,50,2500);
    insert into guest_house values('SAM Super Deluxe Room',50,50,5000);
    insert into guest_house values('VGH Deluxe Room',4,4,2000);
    insert into guest_house values('VGH Super Deluxe Room',50,50,4000);
    """
    run_query(query)

    password1 = 'swapnil'
    password2 = 'rajparikh'
    password3 = 'soumojit'
    password4 = 'sukhomay'
    password5 = 'shashwat'

    password1 = bcrypt.generate_password_hash(password1).decode('utf-8')
    password2 = bcrypt.generate_password_hash(password2).decode('utf-8')
    password3 = bcrypt.generate_password_hash(password3).decode('utf-8')
    password4 = bcrypt.generate_password_hash(password4).decode('utf-8')
    password5 = bcrypt.generate_password_hash(password5).decode('utf-8')
    query = """
    insert into admin (username,password) values
    ('swapnil',%s),
    ('raj',%s),
    ('soumojit',%s),
    ('sukhomay',%s),
    ('shashwat',%s)
    """
    parameters = (password1,password2,password3,password4,password5)
    run_query(query,parameters)

create_tables()