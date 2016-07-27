# Project: Movie Trailer Website
This Project contains the Server Side Code (written in python) to get a List of popuplar movies,movie title,poster image,video trailer from the [MovieDB Api](https://www.themoviedb.org/documentation/api).The Information Gathered from moviedb api is then servered on web page allowing vistor to watch movie information and their corresponding trailer.

**Note:** A test api key of movieDb is created and used in the code.The Api Key is Hardcoded in the code.

## API Method used 
1. [**_discover/movie_**](http://docs.themoviedb.apiary.io/#reference/discover/discovermovie/get) : This method Provide the List of Movies.From the result list following information of the movie is Extracted :
    - Poster Path
    - title
    - overview
     - Movie Id
2. [**_movie/id/videos_**](http://docs.themoviedb.apiary.io/#reference/movies/movieidvideos/get) : This Method is used in program to get a Video Trailer based on the MovieId.Among the List of Video Trailer Always the First Trailer is Extracted.

## Enviroment and Running the Program
- Install Python 2.7.10  
- Download All the Files from the Project.
- Execute launchmovies.py

## Result
A webpage will be opened containing a popular movies.on click of movie poster the movie trailer popups.