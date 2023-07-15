function stickyNavigation() {
  var tabContainer = document.querySelector('.et-hero-tabs-container');
  var tabContainerHeight = tabContainer.offsetHeight;
  var currentId = null;
  var currentTab = null;

  function checkTabContainerPosition() {
    var offset = document.querySelector('.et-hero-tabs').offsetTop + document.querySelector('.et-hero-tabs').offsetHeight - tabContainerHeight;
    if (window.pageYOffset > offset) {
      tabContainer.classList.add('top');
    } else {
      tabContainer.classList.remove('top');
    }
  }

  function findCurrentTabSelector() {
    var newCurrentId = null;
    var newCurrentTab = null;

    document.querySelectorAll('.et-hero-tab').forEach(function (element) {
      var id = element.getAttribute('href');
      var offsetTop = document.querySelector(id).offsetTop - tabContainerHeight;
      var offsetBottom = document.querySelector(id).offsetTop + document.querySelector(id).offsetHeight - tabContainerHeight;

      if (window.pageYOffset > offsetTop && window.pageYOffset < offsetBottom) {
        newCurrentId = id;
        newCurrentTab = element;
      }
    });

  if (currentId !== newCurrentId || currentId === null) {
    currentId = newCurrentId;
    currentTab = newCurrentTab;
    setSliderCss();
  }
}

    function setSliderCss() {
      var width = 0;
      var left = 0;
      if (currentTab) {
        width = getComputedStyle(currentTab).width;
        left = currentTab.offsetLeft;
      }
      document.querySelector('.et-hero-tab-slider').style.width = width;
      document.querySelector('.et-hero-tab-slider').style.left = left + 'px';
    }

  function onScroll() {
    checkTabContainerPosition();
    findCurrentTabSelector();
  }

  function onTabClick(event, element) {
    event.preventDefault();
    var scrollTop = document.querySelector(element.getAttribute('href')).offsetTop - tabContainerHeight + 1;
    window.scrollTo({
      top: scrollTop,
      behavior: 'smooth'
    });
  }

  function initialize() {
    document.querySelectorAll('.et-hero-tab').forEach(function(element) {
      element.addEventListener('click', function(event) {
        onTabClick(event, element);
      });
    });

    window.addEventListener('scroll', onScroll);
  }

  initialize();
}

stickyNavigation();
