const horoscopeDates = {
  Aries: "March 21 - April 19",
  Taurus: "April 20 - May 20",
  Gemini: "May 21 - June 20",
  Cancer: "June 21 - July 22",
  Leo: "July 23 - August 22",
  Virgo: "August 23 - September 22",
  Libra: "September 23 - October 22",
  Scorpio: "October 23 - November 21",
  Sagittarius: "November 22 - December 21",
  Capricorn: "December 22 - January 19",
  Aquarius: "January 20 - February 18",
  Pisces: "February 19 - March 20"
};

var description = document.querySelectorAll('.horoscope_dates');

function keys(obj) {
    return Object.keys(obj);
};

var symbolKeys = keys(horoscopeDates);

description.forEach(function(symbol, index) {
    symbol.textContent = horoscopeDates[symbolKeys[index]];
});


// card movements
var imageOptions = document.querySelectorAll('.horoscope-option');

imageOptions.forEach(function(option) {
  option.addEventListener('click', function() {
    imageOptions.forEach(function(otherOption) {
      otherOption.classList.remove('selected');
    });
    option.classList.add('selected');

    // Select the associated radio button
    var radioBtn = option.querySelector('input[type="radio"]');
    if (radioBtn) {
      radioBtn.checked = true;
    }
  });
});