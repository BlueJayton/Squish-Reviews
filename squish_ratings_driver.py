from flask import *
from dotenv import load_dotenv, find_dotenv
import random
import squish_ratings_functions

load_dotenv(find_dotenv())

app = Flask(__name__)

list_of_movies = ["Scott Pilgrim vs. the World", "Pan's Labyrinth", "The Departed", "The Shawshank Redemption", "Django Unchained", 
                  "Spider-Man: Into the Spider-Verse", "Inglorious Basterds", "Mad Max: Fury Road", "Troll 2", "Hot Fuzz"]

#Make url dict for TMDB API
TMDB_URL_DICT = {"TMDB_BASE_URL" : "https://api.themoviedb.org/3",
                 "TMDB_SEARCH_PATH" : "/search/movie?api_key=",
                 "TMDB_GENRE_PATH" : "/genre/movie/list?api_key=",}

IMG_BASE_URL = "https://image.tmdb.org/t/p/original/"

#MediaWiki API URL dict
WIKI_URL_DICT = {"WIKI_BASE_URL" : "https://en.wikipedia.org/w/api.php?",
                 "WIKI_URL_PARAMS" : "action=query&format=json&prop=info&generator=allpages&inprop=url&gapfrom="}

@app.route('/', methods = ['POST', 'GET'])
def random_movie():
       
    movie_title = random.choice(list_of_movies)
    movie_title_url = squish_ratings_functions.make_url_title(movie_title)
    movie_info = squish_ratings_functions.get_movie_info_TMDB(movie_title_url, TMDB_URL_DICT, WIKI_URL_DICT, IMG_BASE_URL)
        
    if "Random Movie: Dev's Favorites" in request.form.values():
        return redirect(url_for("random_movie"))
    elif 'Search' in request.form.values():
        movie_title = request.form.get("search_text")
        movie_title_url = squish_ratings_functions.make_url_title(movie_title)
        return redirect(url_for("search", movie_title_url = movie_title_url))
        
    
    return render_template (
        "randommovie.html",
        movie_info = movie_info,
    )
    
@app.route('/search/<movie_title_url>', methods = ['POST', 'GET'])
def search(movie_title_url):
    
    movie_info = squish_ratings_functions.get_movie_info_TMDB(movie_title_url, TMDB_URL_DICT, WIKI_URL_DICT, IMG_BASE_URL)
    
    if "Random Movie: Dev's Favorites" in request.form.values():
        return redirect(url_for("random_movie"))
    elif 'Search' in request.form.values():
        movie_title = request.form.get("search_text")
        movie_title_url = squish_ratings_functions.make_url_title(movie_title)
        return redirect(url_for("search", movie_title_url = movie_title_url)) 
       
    return render_template (
        "searchmovie.html",
        movie_info = movie_info
    )    
    
app.run(debug = True)