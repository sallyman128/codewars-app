from flask import Flask
from models.analytics import Analytics
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Analyzer!'

@app.route('/fetchcodewars')
def fetchCodewars():
    username = "sallyman128"
    api_data = fetch_data_from_codewars(username)

    if api_data:
        name = api_data['name']
        leaderboardPosition = api_data['leaderboardPosition']
        languages = api_data['ranks']['languages']
        topLanguage = max(languages, key=lambda lang: languages[lang]["score"])

        analytics = Analytics(name, leaderboardPosition, languages, topLanguage)
        return json.dumps(analytics.to_dict())
    else:
        return "Error fetching data from Codewars"

def fetch_data_from_codewars(username):
    api_url = f'https://www.codewars.com/api/v1/users/{username}'
    print(api_url)
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error: No response from codewars")
        return None

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5001, debug=True)