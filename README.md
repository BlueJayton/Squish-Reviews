<img src="https://github.com/BlueJayton/project1-jayton-schreiner/blob/main/SQUISHreviewswhitebg.png" width="1000" height="auto" title="Squish Reviews. My girlfriend made this logo.">

# [Squish Reviews](https://squish-reviews.fly.dev)
## A Website where you can tell the rating of a movie by how squished it's poster is!

This website was made with Python and Flask. It uses the TMDB API to retrieve information about movies and the MediaWiki API to get the wikipedia page for the movie.

Libraries used include dotenv, random, os, requests, flask-sqlalchemy, flask-login and urllib.

Bootstrap scripts and css were used in order to make a dismissable alert that showed flask flash messages whenever a movie was not successfully found by the TMDB API.

Postgres and SQLAlchemy were used to store users and comments left by said users.

The website will start with a randomly selected movie from a list of 10 of my favorite movies. To get a new one, refresh the page or hit the "Random Movie" button.

Using the search text entry box and the search button, you can search for any movie via the TMDB API.

Depending on the rating of the movie, the poster for the movie will be squished. The worse the rating, the more squished it'll be. </br></br>

 

In order to fork this and have it ready to be used, you should install all of the languages, frameworks, and libraries above, and get an API key for TMDB.
The API key should be kept in your .env (which should be in your .gitignore) and make sure that the name of the API key in the .env matches the one in the code.
Likewise, you will need to create a secret key and have it match the name in the code.

Milestone 1:

One major technical issue was that I kept getting failed deployments due to packages and dependencies not being able to download. To fix this, I installed pipdeptree with pip and used it to delete every single package that wasn't explicitly needed for the project.

Another issue is that I wanted the title of the movie to be in the url whenever a search was done, that way you can send links to other people that take you to specific movies. In order to accomplish this, I had to learn how to do flask redirects and how to pass variables with them. </br></br>

The first persisting problem is that the wiki links aren't 100% accurate. "Room" is a movie, but if you click the wiki link, it takes you to "Room" as in the architecture. In the future, I will try to fix this. 

The other problem is that the site took so much work for functionality that I didn't have a lot of time for aesthetics. I will work to make the site look a lot better soon.

Milestone 2:

The main major issue that I had was that I had apparently grabbed the wrong link when creating the db and thus could not connect to or manipulate my database in any way for the longest time. They way I had to fix this was deleting both the website and the database and remaking them, making sure to grab the correct information the second time.

Another issue that took a lot of time for me to figure out was how to handle multiple html forms through flask. It turned out that the easiest way was to use "if 'button_name' in request.form:" to tell which button was being pressed so that the website could respong accordingly.

One persisting issue is that comments cannot be made on the random movie screen. When I tried to implement this, it would always change what movie was presented when hitting the comment button instead of switching to the search page like it is supposed to. I will attempt to fix this in the future.

Another issue, similar to milestone 1, is that I was very strapped for time on this project and couldn't devote the time I wanted to in order to make the website look aesthetically pleasing.
