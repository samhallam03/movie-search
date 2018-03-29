#!/usr/bin/env python3
import requests
import argparse
from urllib.parse import quote_plus
import platform

from flask import Flask, render_template, request

__version__ = "0.3.1"
app = Flask(__name__)

parser = argparse.ArgumentParser(description='Search for movies')
parser.version = "Movie Search {} on {}".format(__version__, platform.platform())
parser.add_argument('--key', type=str, nargs=1, required=True)
parser.add_argument('--version', action='version')

args = parser.parse_args()
api_key = args.key


@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        search_query = quote_plus(request.form['movie'])
        req = requests.get("http://omdbapi.com/?t={}&apikey={}".format(search_query, api_key[0]))
        movie = req.json()
        return render_template("home.html", movie=movie)
    else:
        return render_template("home.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3333)


