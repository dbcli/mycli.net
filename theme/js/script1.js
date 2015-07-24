(function ($) {
  // Get the .gif images from the "data-alt".
  var getAltImgs = function () {
    var altImgs = []
    $('img').each(function () {
      var data = $(this).data('alt')
      altImgs.push(data)
    })
    return altImgs
  }

  var gif = getAltImgs()

  // Preload all the gif images.
  var image = []

  $.each(gif, function (index) {
    image[index] = new Image()
    image[index].src = gif[index]
  })

  // Change the image to .gif when clicked and vice versa.
  $('figure').on('click', function () {
    var self = $(this),

    $img = self.children('img'),
    $imgSrc = $img.attr('src'),
    $imgAlt = $img.attr('data-alt'),
    $imgExt = $imgAlt.split('.').pop()

    if ($imgExt === 'gif') {
      $img.attr('src', $img.data('alt')).attr('data-alt', $imgSrc)
    } else {
      $img.attr('src', $imgAlt).attr('data-alt', $img.data('alt'))
    }

    // Add play class to help with the styling.
    self.toggleClass('play')

  })

}) (jQuery)
