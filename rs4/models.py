from rs4 import app
from flask_bcrypt import Bcrypt
import psycopg2
from prettytable import PrettyTable
bcrypt = Bcrypt()

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
    result = cursor.fetchall()
    return result

def print_query_output(output, attributes):
    table = PrettyTable()
    table.field_names = attributes
    for row in output:
        table.add_row(row)
    print("\nQuery Output:")
    print(table)


def authenticate(username, password, role):
    print("Authenticate called")
    if role == 'student':
        try:

            cursor.execute("SELECT password FROM student WHERE username = %s", (username,))
            passwords = cursor.fetchone()
            if(len(passwords) == 0):
                return False
            hashed_password = passwords[0]
            if bcrypt.check_password_hash(hashed_password, password):
                return True
            else:
                return False

        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)
            return False
    elif role == 'participant':
        try:
            cursor.execute("SELECT password FROM participant WHERE username = %s", (username, ))
            passwords = cursor.fetchone()
            if(len(passwords) == 0):
                return False
            hashed_password = passwords[0]
            if bcrypt.check_password_hash(hashed_password, password):
                return True
            else:
                return False

        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)
            return False

    elif role == 'organizer':
        try:
            cursor.execute("SELECT password FROM organizer WHERE username = %s", (username,))
            passwords = cursor.fetchone()
            if(len(passwords) == 0):
                return False
            hashed_password = passwords[0]

            if bcrypt.check_password_hash(hashed_password, password):
                return True
            else:
                return False

        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)
            return False
    else:
        try:
            cursor.execute("SELECT password FROM admin WHERE username = %s", (username,))
            passwords = cursor.fetchone()
            if(len(passwords) == 0):
                return False
            hashed_password = passwords[0]

            if bcrypt.check_password_hash(hashed_password, password):
                return True
            else:
                return False

        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)
            return False

class current_user_cls:
    def __init__(self,name,authentication) -> None:
        self.name = name
        self.is_authenticated = authentication

with app.app_context():
    # create_tables()
    pass


