import flask
import os
import requests
from dotenv import load_dotenv, find_dotenv
import random

load_dotenv(find_dotenv())

app = flask.Flask(__name__)

list_of_movies = ["Scott%20Pilgrim%20vs.%20the%20World", "Pan%27s%20Labyrinth", "The%20Departed", "The%20Shawshank%20Redemption", "Django%20Unchained", 
                  "Spider-Man:%20Into%20the%20Spider-Verse", "Inglorious%20Basterds", "Mad%20Max:%20Fury%20Road", "Troll%202", "Hot%20Fuzz"]

#Make url vars for TMDB API
TMDB_BASE_URL = "https://api.themoviedb.org/3"
TMDB_SEARCH_PATH = "/search/movie?api_key="
TMDB_GENRE_PATH = "/genre/movie/list?api_key="
IMG_BASE_URL = "https://image.tmdb.org/t/p/original/"

#Make url vars for MediaWiki API
WIKI_BASE_URL = "https://en.wikipedia.org/w/api.php?"
WIKI_URL_PARAMS = "action=query&format=json&prop=info&generator=allpages&inprop=url&gapfrom="

@app.route('/')
def driver():
    movie = random.choice(list_of_movies)
    TMDB_API_KEY = os.getenv("TMDB_API_KEY")
    TMDB_QUERY = "&language=en-US&query=" + movie + "&page=1&include_adult=false"
    
    TMDB_genre_response = requests.get(
        TMDB_BASE_URL + TMDB_GENRE_PATH + TMDB_API_KEY + "&language=en-US"
    )
    
    genres_response = TMDB_genre_response.json()["genres"]
    
    TMDB_response = requests.get(
        TMDB_BASE_URL + TMDB_SEARCH_PATH + TMDB_API_KEY + TMDB_QUERY
    )
    
    wiki_link_response = requests.get (
        WIKI_BASE_URL + WIKI_URL_PARAMS + movie + "&gaplimit=5"
    )
    
    movie_info = TMDB_response.json()["results"]
    
    #tmdb info
    title = movie_info[0]["title"]
    description = movie_info[0]["overview"]
    poster_link = IMG_BASE_URL + movie_info[0]["poster_path"]
    #rating times .1 to make a percentage from 0 to 1
    rating = round(movie_info[0]["vote_average"], 1)
    rating_from_0_to_1 = rating *.1
    height_calc = 750 * rating_from_0_to_1
    poster_height = str(height_calc) + "px"
    
    #genre info
    list_of_genre_ids = movie_info[0]["genre_ids"]
    genre_list = []
    for index in range(len(genres_response)):
        for genre_id in list_of_genre_ids:
            if genres_response[index]["id"] == genre_id:
                genre_list.append(genres_response[index]["name"])
    genre_string = ', ' .join(genre_list)
        
    #wiki info
    wiki_page_id = list(wiki_link_response.json()["query"]["pages"]) [0]
    wiki_link = wiki_link_response.json()["query"]["pages"][wiki_page_id]["fullurl"]
    
    print(title)
    print(rating)

    return flask.render_template (
        "webpage.html",
        title = title,
        genre_string = genre_string,
        description = description,
        poster_link = poster_link,
        poster_height = poster_height,
        wiki_link = wiki_link,
        rating = rating
    )
    
app.run(debug = True)