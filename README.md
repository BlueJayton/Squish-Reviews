<img src="https://github.com/BlueJayton/project1-jayton-schreiner/blob/main/static/SQUISHreviewswhitebg.png" width="1000" height="auto" title="Squish Reviews. My girlfriend made this logo.">

# [Squish Reviews](https://squish-reviews.fly.dev)
## A Website where you can tell the rating of a movie by how squished it's poster is!

This website was made with Python and Flask. It uses the TMDB API to retrieve information about movies.

Libraries used include dotenv, random, os, requests, flask-sqlalchemy, flask-login and urllib.

Bootstrap scripts and css were used in order to make a dismissable alert that showed flask flash messages whenever a movie was not successfully found by the TMDB API.

The website will start with a randomly selected movie from a list of 10 of my favorite movies. To get a new one, refresh the page or hit the "Random Movie" button.

Using the search text entry box and the search button, you can search for any movie via the TMDB API.

Depending on the rating of the movie, the poster for the movie will be squished. The worse the rating, the more squished it'll be. </br></br>

 

In order to fork this and have it ready to be used, you should install all of the languages, frameworks, and libraries above, and get an API key for TMDB.
The API key should be kept in your .env (which should be in your .gitignore) and make sure that the name of the API key in the .env matches the one in the code.
Likewise, you will need to create a secret key and have it match the name in the code.
