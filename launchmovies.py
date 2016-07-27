import json
import moviesInfo
import fresh_tomatoes
from urllib2 import Request, urlopen

headers = {
 'Accept': 'application/json'
}
# The MovieDB Account Api Key
moviedb_api_key = "2f0551b37ac2ff1818f4597bd295affa"

"""This Methods gets a JSON Response by MovieDB Api Url."""


def getJsonResponsebyUrl(url):
        # Url is Appeneded with moviedb api key and is passed to request
        request = Request(url+moviedb_api_key, headers=headers)
        response_body = urlopen(request).read()
        return json.loads(response_body)  # response body is converted to json

"""This Method is used to get first movie Trailerkey based on MovieID. """


def getMovieTrailerById(movie_id):
    # getJsonReponsebyUrl Method is Invoked and
    # List of Videos are Returned as Response
    trailerList = getJsonResponsebyUrl(
        "https://api.themoviedb.org/3/movie/" + str(
            movie_id) + "/videos?api_key=")['results']
    return trailerList[0]['key']

# The Popular Movie Information is Extracted by invoking
# discover/movie method of MovieDB api.The List contains
# Information like posterPath,Movie Title,Movie Overview,MovieId
json_movie_list = getJsonResponsebyUrl(
    "http://api.themoviedb.org/3/discover/movie?api_key=")['results']

# the JsonList is Iterated to extract the Information
# like posterpath,title,overview,movieId
# A new movies object is contructed which will be passed to frsh_tomatoes
movies = []
for movieDetails in json_movie_list:
    poster_path = "https://image.tmdb.org/t/p/w640/"+movieDetails[
        'poster_path']
    movie_id = movieDetails['id']
    # getMovieTrailerbyID is invoked and videoId is returned.
    video_id = getMovieTrailerById(movie_id)
    # Youtube Video Url is Constructed
    video_url = "https://www.youtube.com/watch?v="+video_id
    # ArrayList of Movie Object is Contructed
    # which has to be passed to freshTomatoes
    movieobj = moviesInfo.Movie(
        movieDetails['title'], movieDetails['overview'],
        poster_path, video_url)
    movies.append(movieobj)
# open movie page of Fresh Tomatoes is Invoked.
fresh_tomatoes.open_movies_page(movies)
