import os
import requests
from urllib import parse

def make_url_title (movie_title):
    return parse.quote(movie_title)

def get_movie_info_TMDB (movie, TMDB_URL_DICT, WIKI_URL_DICT, IMG_BASE_URL):
    
    movie_info = {"title" : "", "description": "",
                  "poster_link" : "", "poster_height" : "",
                  "rating" : "", "genre_string" : "",
                  "wiki_link" : "", "movie_id" : ""}
    
    TMDB_API_KEY = os.getenv("TMDB_API_KEY")
    TMDB_QUERY = "&language=en-US&query=" + movie + "&page=1&include_adult=false"
    
    TMDB_genre_response = requests.get(
        TMDB_URL_DICT['TMDB_BASE_URL'] + TMDB_URL_DICT['TMDB_GENRE_PATH'] + TMDB_API_KEY + "&language=en-US"
    )
    
    genres_response = TMDB_genre_response.json()["genres"]
    
    TMDB_response = requests.get(
        TMDB_URL_DICT['TMDB_BASE_URL'] + TMDB_URL_DICT['TMDB_SEARCH_PATH'] + TMDB_API_KEY + TMDB_QUERY
    )
    
       
    movie_request_json = TMDB_response.json()["results"]
    if movie_request_json == []:
        print("Movie not found")
        return False
    
    #tmdb info
    movie_info["title"] = movie_request_json[0]["title"]
    movie_info["description"] = movie_request_json[0]["overview"]
    movie_info["poster_link"] = IMG_BASE_URL + movie_request_json[0]["poster_path"]
    movie_info["movie_id"] = movie_request_json[0]["id"]
    #rating times .1 to make a percentage from 0 to 1
    movie_info["rating"] = round(movie_request_json[0]["vote_average"], 1)
    rating_from_0_to_1 = movie_info["rating"] *.1
    height_calc = 700 * rating_from_0_to_1
    movie_info["poster_height"] = str(height_calc) + "px"
    
    #genre info
    list_of_genre_ids = movie_request_json[0]["genre_ids"]
    genre_list = []
    for index in range(len(genres_response)):
        for genre_id in list_of_genre_ids:
            if genres_response[index]["id"] == genre_id:
                genre_list.append(genres_response[index]["name"])
    movie_info["genre_string"] = ', ' .join(genre_list)
    
    movie_info["wiki_link"] = get_wiki_link(movie, WIKI_URL_DICT)
    
    return movie_info

def get_wiki_link (movie, WIKI_URL_DICT):
    
    wiki_link_response = requests.get (
        WIKI_URL_DICT['WIKI_BASE_URL'] + WIKI_URL_DICT['WIKI_URL_PARAMS'] + movie + "&gaplimit=5"
    )
    
    wiki_page_id = list(wiki_link_response.json()["query"]["pages"]) [0]
    
    return wiki_link_response.json()["query"]["pages"][wiki_page_id]["fullurl"]