from flask import *
import os
from dotenv import load_dotenv, find_dotenv
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
import random
import squish_reviews_functions

load_dotenv(find_dotenv())

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
    return Person.query.get(int(id))

#DATABASE MODELS
class Person(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    
    def is_active(self):
        return True
    
class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    movieid = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(1000), nullable=False)

with app.app_context():
    db.create_all()
    
    

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
def home():
    if request.method == 'POST':
        if "Login" in request.form.values():
            username = request.form.get("username")
            return redirect(url_for("login", username=username))
    
        if "Register" in request.form.values():
            username = request.form.get("username")
            return redirect(url_for("register", username=username))
    
    return render_template (
        "home.html"
    )

@app.route('/login')
def login():
    username = request.args.get('username')
    user = Person.query.filter_by(username=username).first()
    
    if user:
        login_user(user)
        return redirect(url_for('random_movie'))
    else:
        flash("No user found.")
        return redirect(url_for("home"))
    

@app.route('/register')
def register():
    username = request.args.get('username')
    user = Person.query.filter_by(username=username).first()
    
    if user:
        flash("User already exists.")
        return redirect(url_for('home'))
    elif user is None:
        user = Person(username=username)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for("random_movie"))
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route('/random', methods = ['POST', 'GET'])
def random_movie():
       
    movie_title = random.choice(list_of_movies)
    movie_title_url = squish_reviews_functions.make_url_title(movie_title)
    movie_info = squish_reviews_functions.get_movie_info_TMDB(movie_title_url, TMDB_URL_DICT, WIKI_URL_DICT, IMG_BASE_URL)
    movie_title = movie_info["title"]
    comments = Comments.query.filter_by(movieid = movie_info["movie_id"])
    
    if movie_info == False:
        flash("No movie Found.")
        movie_title = random.choice(list_of_movies)
        movie_title_url = squish_reviews_functions.make_url_title(movie_title)
        movie_info = squish_reviews_functions.get_movie_info_TMDB(movie_title_url, TMDB_URL_DICT, WIKI_URL_DICT, IMG_BASE_URL)
        return render_template (
            "randommovie.html",
            movie_info = movie_info,
            curr_user = current_user.username,
            comments = comments,
        )
    

    if "random_movie" in request.form:
        return redirect(url_for("random_movie"))
    elif "search_button" in request.form:
        movie_title = request.form.get("search_text")
        movie_title_url = squish_reviews_functions.make_url_title(movie_title)
        return redirect(url_for("search", movie_title_url = movie_title_url))
    elif "logout_button" in request.form:
        return redirect(url_for("logout"))
    
    return render_template (
        "randommovie.html",
        movie_info = movie_info,
        curr_user = current_user.username,
        comments = comments,
    )
   
@app.route('/search/<movie_title_url>', methods = ['POST', 'GET'])
def search(movie_title_url):
    
    movie_info = squish_reviews_functions.get_movie_info_TMDB(movie_title_url, TMDB_URL_DICT, WIKI_URL_DICT, IMG_BASE_URL)
    comments = Comments.query.filter_by(movieid = movie_info["movie_id"])
    
    if movie_info == False:
        flash("No movie Found.")
        return redirect(url_for("random_movie"))
    
    if "random_movie" in request.form:
        return redirect(url_for("random_movie"))
    elif "search_button" in request.form:
        movie_title = request.form.get("search_text")
        movie_title_url = squish_reviews_functions.make_url_title(movie_title)
        return redirect(url_for("search", movie_title_url = movie_title_url))
    elif "logout_button" in request.form:
        return redirect(url_for("logout"))
    
    if "make_comment" in request.form:
        comment_post = Comments(movieid = movie_info["movie_id"], username = current_user.username, rating = request.form.get("user_rating"), comment = request.form.get("comment") )
        
        db.session.add(comment_post)
        db.session.commit()
        
        movie_title = movie_info["title"]
        movie_title_url = squish_reviews_functions.make_url_title(movie_title)
        return redirect(url_for("search", movie_title_url = movie_title_url))
    
       
    return render_template (
        "searchmovie.html",
        movie_info = movie_info,
        curr_user = current_user.username,
        comments = comments,
    )    