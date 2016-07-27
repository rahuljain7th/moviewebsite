""" A Movie Class Which Stores the Following Movie Information:
    title,description,imagepath,trailer_url"""


class Movie:
    def __init__(self, movie_title, movie_description,
                 movie_box_art, movie_trailer_url):
        self.title = movie_title
        self.storyline = movie_description
        self.poster_image_url = movie_box_art
        self.trailer_youtube_url = movie_trailer_url
