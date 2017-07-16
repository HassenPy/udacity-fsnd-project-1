$(function(){
  // Pause the video when the modal is closed
  $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
      // Remove the src so the player itself gets removed, as this is the only
      // reliable way to ensure the video stops playing in IE
      $("#trailer-video-container").empty();
      console.log('opened');
  });

  // Start playing the video whenever the trailer modal is opened
  $('.watch').on('click', function (event) {
      console.log('clicked!');
      var trailerYouTubeId = $(this).attr('data-trailer-youtube-id');
      var sourceUrl = 'https://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
      $("#trailer-video-container").empty().append($("<iframe></iframe>", {
        'id': 'trailer-video',
        'type': 'text-html',
        'src': sourceUrl,
        'frameborder': 0
      }));
  });
});
