import requests
from models import db, Language

def fetch_data_from_codewars():
    api_url = "https://www.codewars.com/api/v1/users/sallyman128"
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error: No response from codewars")
        return None

def insert_data_into_db(languages):
    for language in languages:
        color = languages[language]['color']
        score = languages[language]['score']
        l = Language(language=language, color=color, score=score)
        db.session.add(l)
    db.session.commit()

def add_daily_data_from_codewars():
    api_data = fetch_data_from_codewars()
    if api_data:
            # Insert data into the database
            insert_data_into_db(api_data['ranks']['languages'])