"""Movie page html template shunks."""

# Styles and scripting for the page.
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta charset="utf-8">
    <title>Hassen's movie trailers!</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="./static/css/bootstrap.min.css">
    <link rel="stylesheet" href="./static/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="./static/css/main.css">
    <link rel="stylesheet" href="./static/css/animate.css">
    <link href="https://fonts.googleapis.com/css?family=Bellefair|Slabo+27px" rel="stylesheet">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="./static/js/bootstrap.min.js"></script>
    <script src="./static/js/main.js"></script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    <!-- Main Page Content -->
    <div class="navbar navbar-fixed-top" role="navigation">
    <div class="container">
      <div class="navbar-header">
        <a class="navbar-brand">Hassen's movie trailers!</a>
      </div>
    </div>
    </div>
    <ul class="movies container list-inline">
      {movie_tiles}
    </ul>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<li>
    <div class="movie-tile animated {favorite} text-center"
    >
        <div class="img-wrapper center-block">
            <img src="{poster_image_url}" width="220" height="342">
        </div>
        <div class="movie-data center-block animated fadeIn">
            <div class="rating">I rate: <span>{rating}</span>/10</div>
            <div>{storyline}</div>
            <button class="watch"
                    data-trailer-youtube-id="{trailer_youtube_id}"
                    data-toggle="modal" data-target="#trailer"
            >
            Watch trailer</button>
        </div>
        <h3>{movie_title}</h3>
    </div>
</li>
'''
