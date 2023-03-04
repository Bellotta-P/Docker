from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash,  render_template, Response
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import pymssql
import pandas as pd
from bson import json_util
import json


import psycopg2 
import psycopg2.extras

app = Flask(__name__)

app.secret_key = 'xyzsdfg'

def connection():
    conn = pymssql.connect(server = '213.140.22.237\SQLEXPRESS',user = 'bellotta.pietro',password = 'xxx123##',database = 'bellotta.pietro')
    return conn


mysql = MySQL(app)
CORS(app)


@app.route('/')
def index():
    return ("je")

@app.route('/Docenti')
def get_data():
    conn = connection()
    cur = conn.cursor(as_dict=True)
    cur.execute("SELECT * FROM Docente")
    list_users = cur.fetchall()
    return jsonify(list_users)
    resp = jsonify(list_users)
    resp = json_util.dumps(list_users)
    return Response(resp, mimetype='application/json')

@app.route('/Verifiche')
def get_data2():
    conn = connection()
    cur = conn.cursor(as_dict=True)
    cur.execute("SELECT * FROM Verifica")
    list_users = cur.fetchall()
    return jsonify(list_users)
    resp = jsonify(list_users)
    resp = json_util.dumps(list_users)
    return Response(resp, mimetype='application/json')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.json['email']
        password = request.json['password']
        conn = connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Docente WHERE email=%s AND password=%s', (email, password))
        user = cursor.fetchone()
        if user:
            return jsonify({"message": "Logged in successfully", "email":email, "password":password}), 200
        else:
            return jsonify("Doesn't match"), 400

    return jsonify({"message": "Error"}), 400


@app.route('/logout')
def logout():
    if 'loggedin' in session:
        session.pop('loggedin', None)
        session.pop('Nome', None)
        session.pop('email', None)
        return jsonify({"message": "Logged out successfully"}), 200
    else:
        return jsonify({"message": "You are not logged in"}), 400
        

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.json['nome']
        cognome = request.json['cognome']
        email = request.json['email']
        password = request.json['password']

        conn = connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Docente WHERE email=%s', (email))
        account = cursor.fetchone()
        if account:
            return jsonify({"message": "Account already exists"}), 400
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            return jsonify({"message": "Invalid email address"}), 400
        elif not nome or not password or not email:
            return jsonify({"message": "Please fill out the form"}), 400
        else:
            cursor.execute(
                'INSERT INTO Docente (nome, cognome, email, password) VALUES (%s, %s, %s, %s)', (nome,cognome, email, password))
            conn.commit()
            return jsonify({"message": "You have successfully registered"}), 201

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)