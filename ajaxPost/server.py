from flask import Flask, request, redirect, render_template, session, flash
import sys

sys.path.append('../')
from sqlconnector.mysqlconnection import MySQLConnector

app = Flask(__name__)

# app.secret_key = "aabbbCdefgh234"
mysql = MySQLConnector(app,'api_ajax') #using the db from friends assignment as this has many users in the db


@app.route('/')
def index():
    return render_template('index.html')



app.run(debug=True)
