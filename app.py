from flask import Flask, jsonify, request, abort
import sqlite3

app = Flask(__name__)

# Database setup fn
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(""
                   "
        
    )