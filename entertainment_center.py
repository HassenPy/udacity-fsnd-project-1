"""Get movies from json then open them in a web page."""
import json


class Movie():
    """A class representation of a movie."""

    def __init__(self, title, storyline, poster, yt_trailer, my_rating):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = yt_trailer
        self.my_rating = my_rating

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


def get_movies():
    """Read movies from a json file."""
    movies_file = open('movies.json', 'r').read()

    # json.loads deserializes a string to python data structure.
    return json.loads(movies_file)


def get_movie_instances():
    """Generate Movie class instances from the movie data."""
    movies = []
    for movie in get_movies():
        # keys order: Movie(title, storyline, poster, yt_trailer, my_rating)
        movies.append(Movie(movie[0], movie[1], movie[2], movie[3], movie[4]))

    return movies
