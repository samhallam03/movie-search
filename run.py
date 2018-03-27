#!/usr/bin/env python3
import requests
import argparse
from urllib.parse import quote_plus
import platform

__version__ = "0.1.1"

parser = argparse.ArgumentParser(description='Search for movies')
parser.version = "Movie Search {} on {}".format(__version__, platform.platform())
parser.add_argument('--key', type=str, nargs=1, required=True)
parser.add_argument('query', metavar='query string', type=str, nargs='+',
                    help='The input to search for')
parser.add_argument('--version', action='version')

args = parser.parse_args()

api_key = args.key
search_query = quote_plus(" ".join(args.query))

req = requests.get("http://omdbapi.com/?t={}&apikey={}".format(search_query, api_key[0]))
movie = req.json()

for key, item in movie.items():
    print(f"{key} : {item}")


