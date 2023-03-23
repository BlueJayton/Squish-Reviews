# project1-jayton-schreiner

![Couldn't find logo](https://github.com/BlueJayton/project1-jayton-schreiner/blob/main/SQUISHreviews.png "Squish Reviews. My girlfriend made this logo")
# [Squish Reviews](https://squish-reviews.fly.dev)
## A Website where you can tell the rating of a movie by how squished it's poster is!

#### This website was made with Python and Flask. It uses the TMDB API to retrieve information about movies and the MediaWiki API to get the wikipedia page for the movie.
#### Libraries use include dotenv, random, os, requests, and urllib.
#### The website will start with a randomly selected movie from a list of 10 of my favorite movies. To get a new one, refresh the page or hit the "Random Movie" button.
#### Using the search text entry box and the search button, you can search for any movie via the TMDB API.
#### Depending on the rating of the movie, the poster for the movie will be squished. The worse the rating, the more squished it'll be.



#### In order to fork this and have it ready to be used, you should install all of the languages, frameworks, and libraries above, and get an API key for TMDB.
#### The API key should be kept in your .env (which should be in your .gitignore) and make sure that the name of the API key in the .env matches the one in the code.

One major technical issue was that I kept getting failed deployments due to packages and dependencies not being able to download. To fix this, I installed pipdeptree with pip and used to delete every single package that wasn't explicitly needed for the project.
Another issue is that I wanted the title of the movie to be in the url whenever a search was done, that way you can send links to other people that take you to specific movies. In order to accomplish this, I had to learn how to do flask redirects and how to pass variables with them. 

The first persisting problem is that the wiki links aren't 100% accurate. "Room" is a movie, but if you click the wiki link, it takes you to Room as in the architecture. IN the future, I will try to fix this. 
The other problem is that the site took so much work for functionalty that I didn't have a lot of time for aesthetics. I will work to make the site look a lot better soon.