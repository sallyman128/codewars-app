#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return 'Analyzer is working'

if __name__ == "__main__":
    app.run(port=3000)