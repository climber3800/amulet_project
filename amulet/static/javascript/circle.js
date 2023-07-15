const amulets = document.querySelectorAll('.amulets');
const circle = document.querySelector('.circle');
const silverText = document.querySelector('.silver-text');
const steelText = document.querySelector('.steel-text');

silverText.addEventListener('click', () => {
  const silverImage = document.querySelector('#silver');

  // Hide all symbols in the circle
  circle.querySelectorAll('img').forEach(symbol => {
    if (symbol.id !== 'runes') {
      symbol.style.display = 'none';
    }
  });

  // Display the silver image in the center of the circle
  if (silverImage) {
    // Add a class to trigger the CSS transition
    silverImage.style.display = 'block';
    silverImage.classList.add('symbol-transition');
    circle.classList.add('animation');

    // Delay the display change to allow the transition to take effect
    setTimeout(() => {
      // Remove the class after the transition completes
      silverImage.classList.remove('symbol-transition');
      circle.classList.remove('animation');
    }, 300);
  }
});

steelText.addEventListener('click', () => {
  const steelImage = document.querySelector('#steel');

  // Hide all symbols in the circle
  circle.querySelectorAll('img').forEach(symbol => {
    if (symbol.id !== 'runes') {
      symbol.style.display = 'none';
    }
  });

  // Display the silver image in the center of the circle
  if (steelImage) {
    // Add a class to trigger the CSS transition
    steelImage.style.display = 'block';
    steelImage.classList.add('symbol-transition');
    circle.classList.add('animation');

    // Delay the display change to allow the transition to take effect
    setTimeout(() => {
      // Remove the class after the transition completes
      steelImage.classList.remove('symbol-transition');
      circle.classList.remove('animation');
    }, 300);
  }
});

amulets.forEach(amulet => {
  amulet.addEventListener('click', () => {
    const amuletId = amulet.getAttribute('id');

    const symbolId = amuletId.replace('1', '');

    // Hide all symbols in the circle
    circle.querySelectorAll('img').forEach(symbol => {
      if (symbol.id !== 'runes') {
        symbol.style.display = 'none';
      }
    });

    // Display the selected symbol in the center of the circle
    const selectedSymbol = document.querySelector(`#${symbolId}`);
    if (selectedSymbol) {
      // Add a class to trigger the CSS transition
      selectedSymbol.style.display = 'block';
      selectedSymbol.classList.add('symbol-transition');
      circle.classList.add('animation');

      // Delay the display change to allow the transition to take effect
      setTimeout(() => {
        // Remove the class after the transition completes
        selectedSymbol.classList.remove('symbol-transition');
        circle.classList.remove('animation');
      }, 300);
    }
  });
});






// Smooth move to Start section when the circle is clicked!

const clickCircle = document.getElementById('click_circle');

clickCircle.addEventListener('click', function(event) {
  event.preventDefault(); // Prevent the default jump-to-anchor behavior

  const targetId = this.getAttribute('href'); // Get the target section's ID

  const targetElement = document.querySelector(targetId); // Find the target element

  if (targetElement) {
    smoothScrollTo(targetElement); // Scroll to the target element smoothly
  }
});

function smoothScrollTo(targetElement) {
  const startPosition = window.pageYOffset; // Get the current scroll position
  const targetPosition = targetElement.getBoundingClientRect().top + startPosition; // Calculate the target position relative to the current scroll position
  const distance = targetPosition - startPosition; // Calculate the distance to scroll
  const duration = 800; // Specify the duration of the scroll animation (in milliseconds)
  const startTime = performance.now(); // Get the start time of the animation

  function scrollStep(currentTime) {
    const elapsedTime = currentTime - startTime; // Calculate the elapsed time
    const progress = Math.min(elapsedTime / duration, 1); // Calculate the animation progress (between 0 and 1)
    const easing = easeInOutCubic(progress); // Apply easing function to control the scroll speed

    window.scrollTo(0, startPosition + distance * easing); // Scroll to the current position based on the easing

    if (elapsedTime < duration) {
      window.requestAnimationFrame(scrollStep); // Continue scrolling animation until the duration is reached
    }
  }

  // Easing function (cubic easing in/out)
  function easeInOutCubic(t) {
    return t < 0.5 ? 4 * t * t * t : (t - 1) * (2 * t - 2) * (2 * t - 2) + 1;
  }

  window.requestAnimationFrame(scrollStep); // Start the scrolling animation
}


// random circle image
document.addEventListener('DOMContentLoaded', function() {
  const images = document.querySelectorAll('img[id^="vegvisir"], img[id^="yggdrasil"], img[id^="valknut"], img[id^="aegishjalmur"]');
  const randomIndex = Math.floor(Math.random() * images.length);
  const randomImage = images[randomIndex];

  randomImage.style.display = 'block';
});
