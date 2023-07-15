var main_frame = document.querySelectorAll('.main_frame');

main_frame.forEach(function(option) {
  var headline_frame = option.querySelector('.headline_frame');
  headline_frame.addEventListener('click', function(event) {
    event.stopPropagation(); // Prevent click event from bubbling up to the parent .main_frame
    option.classList.toggle('selected');
  });
});
