import MySQLdb.cursors
from flask import Flask, jsonify, request, json
import re
from pymongo import MongoClient
import os
from flask_restful import Resource,Api,reqparse
from flask_cors import CORS
import pymssql
import pandas as pd
from bson import json_util
import psycopg2
import psycopg2.extras

app = Flask(__name__)

def connection():
    conn = pymssql.connect(server = '213.140.22.237\SQLEXPRESS',user = 'bellotta.pietro',password = 'xxx123##',database = 'bellotta.pietro')
    return conn

mysql = MySQL(app)
CORS(app)

@app.route('/')
def pagina():
    return 'pagina'

@app.route('/verifiche')
def verifiche():
    conn = connection()
    cur = conn.cursor(as_dict = True)
    cur.execute('SELECT * FROM verifica')
    listaverifiche = cur.fetchall()
    return jsonify(listaverifiche)
    resp = json_util.dumps(listaverifiche)
    return Response(resp,mimetype = 'application/json')

@app.route('/docenti')
def docenti():
    conn = connection()
    cur = conn.cursor(as_dict = True)
    cur.execute('SELECT * FROM docente')
    lista = cur.fetchall()
    return jsonify(lista)
    resp = json_util.dumps(lista)
    return Response(resp,mimetype = 'application/json')

if __name__ == "__main__":
    app.run()