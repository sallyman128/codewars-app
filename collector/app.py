import json
from flask import Flask
import psycopg2
import os
import requests

app = Flask(__name__)
password = os.environ['POSTGRES_PASSWORD']


@app.route('/')
def hello_world():
    return 'Collector working!'

def add_languages():
    api_data = fetch_data_from_codewars()
    languages = api_data['ranks']['languages']
    if api_data:
        with psycopg2.connect(host="db", user="postgres", password=password, database="codewars_db") as conn:
            with conn.cursor() as cur:
                for language in languages:
                    language_data = {
                        'language': language,
                        'color': languages[language]['color'],
                        'score': languages[language]['score'],
                    }
                    cur.execute(f"INSERT INTO languages (language, color, score) VALUES (%(language)s, %(color)s, %(score)s)", language_data)
        conn.close()
    return 'Updated language table'


@app.route('/languages')
def get_languages():
    add_languages()
    with psycopg2.connect(host="db", user="postgres", password=password, database="codewars_db") as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM languages")
            row_headers = [x[0] for x in cur.description]
            results = cur.fetchall()
    conn.close()

    json_data = [dict(zip(row_headers, result)) for result in results]
    return json_data


@app.route('/initdb')
def db_init():
    conn = psycopg2.connect(host="db", user="postgres", password=password)
    conn.set_session(autocommit=True)
    with conn.cursor() as cur:
        cur.execute("DROP DATABASE IF EXISTS codewars_db")
        cur.execute("CREATE DATABASE codewars_db")
    conn.close()

    with psycopg2.connect(host="db", user="postgres", password=password, database="codewars_db") as conn:
        with conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS language")
            cur.execute('''
                CREATE TABLE languages (
                    id SERIAL PRIMARY KEY,
                    language VARCHAR,
                    color VARCHAR,
                    score INTEGER,
                    date DATE DEFAULT CURRENT_DATE
                );
            ''')
    conn.close()

    return 'init database'

def fetch_data_from_codewars():
    api_url = "https://www.codewars.com/api/v1/users/sallyman128"
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error: No response from codewars")
        return None
