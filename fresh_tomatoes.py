"""This module deals with formatting the html shunks of the movie website."""
import webbrowser
import os
import re

from entertainment_center import get_movie_instances
from template import main_page_head, main_page_content, movie_tile_content


def create_movie_tiles_content(movies):
    """Return formatted html for the movies list."""
    # The HTML content for this section of the page
    content = ''

    # Orders the movies list by my_rating and gets the highest rated movie.
    # Adapted the student_tuples example in this link:
    # https://docs.python.org/3/howto/sorting.html#key-functions
    favorite = sorted(movies, key=lambda m: m.my_rating)[-1]
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)

        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the favorite tile first
        if favorite == movie:
            content = movie_tile_content.format(
                movie_title=movie,
                poster_image_url=movie.poster_image_url,
                trailer_youtube_id=trailer_youtube_id,
                storyline=movie.storyline,
                favorite='favorite',
                rating=movie.my_rating
            ) + content
        else:
            # Append the tile for the movie with its content filled in
            content += movie_tile_content.format(
                movie_title=movie,
                poster_image_url=movie.poster_image_url,
                trailer_youtube_id=trailer_youtube_id,
                storyline=movie.storyline,
                favorite='',
                rating=movie.my_rating
            )
    return content


def open_movies_page(movies):
    """Create and open the main movies html page."""
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)


if __name__ == "__main__":
    open_movies_page(get_movie_instances())
