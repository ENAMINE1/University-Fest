from flask import Flask
# import psycopg2
app = Flask(__name__, template_folder='templates')
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tccs.db'
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
from rs4 import routes