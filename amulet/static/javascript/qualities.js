var options = document.querySelectorAll('.quality_name input[type="checkbox"]');
var selectedCount = 0;
var firstSelectedIndex = -1;
var selectedIndex = [-1, -1, -1];

document.addEventListener('DOMContentLoaded', function() {
  options.forEach(function(checkbox) {
    checkbox.checked = false;
  });

  options.forEach(function(checkbox, index) {
    checkbox.addEventListener('change', function() {
      var parent = this.closest('.quality_option');
      if (this.checked) {
        if (selectedCount < 3) {
          parent.classList.add('selected');
          selectedCount++;
          if (selectedCount === 1) {
            firstSelectedIndex = index;
            selectedIndex[0] = index;
          }
          if (selectedCount === 2) {
            selectedIndex[1] = index;
          }
          if (selectedCount === 3) {
            selectedIndex[2] = index;
          }

        } else {
          options[firstSelectedIndex].checked = false;
            var firstSelectedParent = options[firstSelectedIndex].closest('.quality_option');
            firstSelectedParent.classList.remove('selected');
          parent.classList.add('selected');
          firstSelectedIndex = selectedIndex[1];
          selectedIndex[0] = selectedIndex[1];
          selectedIndex[1] = selectedIndex[2];
          selectedIndex[2] = index;
        }

      } else {
        parent.classList.remove('selected');
        selectedCount--;
        if (index === selectedIndex[0]) {
          firstSelectedIndex = selectedIndex[1];
          selectedIndex[0] = selectedIndex [1];
          selectedIndex [1] = selectedIndex [2];
          selectedIndex[2] = -1;
        } else if (index === selectedIndex[1]) {
          selectedIndex[1] = selectedIndex[2];
          selectedIndex[2] = -1;
        } else if (index === selectedIndex[2]) {
          selectedIndex[2] = -1;
        }
      }
    });
    var container = checkbox.closest('.quality_option');
    container.addEventListener('click', function(event) {
        if (event.target.tagName.toLowerCase() !== 'input') {
            checkbox.checked = !checkbox.checked;
            checkbox.dispatchEvent(new Event('change'));
        }
    });
  });
});
