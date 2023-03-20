import flask
import os
import requests
from dotenv import load_dotenv, find_dotenv
import random

load_dotenv(find_dotenv())

list_of_movies = ["Scott%20Pilgrim%20vs.%20the%20World", "Pan%27s%20Labyrinth", "The%20Departed"]

#Make url vars for TMDB API
TMDB_BASE_URL = "https://api.themoviedb.org/3"
TMDB_PATH = "/search/movie?api_key="

#Make url vars for MediaWiki API


#app = flask.Flask(__name__)

#@app.route('/')
def driver():
    movie = random.choice(list_of_movies)
    TMDB_API_KEY = os.getenv("TMDB_API_KEY")
    TMDB_QUERY = "&language=en-US&query=" + movie + "&page=1&include_adult=true"
    
    response = requests.get(
        TMDB_BASE_URL + TMDB_PATH + TMDB_API_KEY + TMDB_QUERY
    )
    
    movie_info = response.json()["results"]
    
    title = movie_info[0]["original_title"]
    description = movie_info[0]["overview"]
    
    print(title)
    print(description)
    
    #return flask.render_template (
        #"webpage.html"
    #)
    
#app.run(debug = True)
driver()