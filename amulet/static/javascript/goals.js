// Add description to cards
const goalsDictionary = {
  career_advancement: "Securing promotions, increasing your income, starting or expanding your own business, obtaining higher-level positions, and gaining recognition within your industry.",
  financial_stability: "Achieving a desired level of income, managing and reducing debts, increasing savings and investments, improving credit scores, and establishing a sustainable budget.",
  educational_achievement: "Obtaining a degree or advanced certification in your desired field, pursuing further education or specialized training to enhance your knowledge and skills.",
  personal_growth: "Cultivating self-awareness, enhancing emotional intelligence, developing effective communication and interpersonal skills, setting and achieving personal goals.",
  healthy_lifestyle: "Adopting a balanced and nutritious diet, establishing a regular exercise routine, maintaining a healthy weight, prioritizing mental well-being through stress management techniques and self-care practices.",
  strong_relationships: "Building strong relationships, investing quality time and effort in nurturing personal connections, creating a supportive network of meaningful relationships that contribute to personal happiness and fulfillment.",
  life_partner: "Clarifying your values and relationship preferences and ultimately establishing a loving and supportive partnership based on mutual respect, trust, and shared goals for the future.",
  travel_exploration: "Embarking on adventurous journeys to diverse destinations, discovering hidden gems and iconic landmarks, expanding your worldview through cross-cultural interactions.",
  owning_home: "Acquiring a home that reflects your personal style, purchasing a vehicle of your dream, investing in high-quality and functional items that bring joy and efficiency to your daily life.",
  starting_family: "Building a strong foundation of love and commitment, creating a nurturing and supportive home environment, making decisions about starting a family, such as having children or adopting.",
  independent_life: "Having an independent, private life with sexual freedom, maintaining boundaries and privacy, making choices regarding intimate relationships and sexual expression that align with individual desires and values.",
  social_boundaries: "Challenging societal norms and biases, promoting inclusivity and equality, embracing diversity, fostering a society where individuals are valued regardless of their background, identity, or characteristics.",
  overcoming_fears: "Identifying and challenging negative thought patterns, taking gradual steps outside of your comfort zone, and embracing a mindset of self-belief and resilience to unlock your full potential.",
  mindfulness_inner_peace: "Practicing present-moment awareness, embracing meditation and mindful techniques, nurturing a sense of inner calm and tranquility and cultivating a state of balance and harmony in daily life.",
  positive_impact: "Acts of kindness and compassion, supporting and uplifting those in need, volunteering time and resources for community service and inspiring positive change in the lives of individuals and communities.",
  pursuing_passion: "Dedicating time and effort to engaging in activities that bring joy and fulfillment, exploring interests and talents, honing skills, and fostering personal growth and creative expression.",
  mental_wellbeing: "Prioritizing self-care, practicing stress management techniques, fostering positive relationships and connections, seeking support when needed, engaging in activities that promote relaxation and self-reflection.",
  closertoGod: "Deepening one's spiritual connection, engaging in prayer or meditation, participating in religious or spiritual practices, seeking guidance and wisdom, and cultivating a personal relationship with the divine.",
  sustainable_lifestyle: "Making conscious choices to reduce environmental impact, adopting sustainable practices such as recycling and conservation, and actively contributing to the preservation and protection of our planet.",
  purpose_meaning: "Exploring personal values and aspirations, reflecting on life's significance, discovering one's unique strengths and passions, aligning actions with core values, and creating a fulfilling and meaningful life path.",
};

var description = document.querySelectorAll('.goal_description');
function keys(obj) {
    return Object.keys(obj);
};
var goalKeys = keys(goalsDictionary);
description.forEach(function(goal, index) {
    goal.textContent = goalsDictionary[goalKeys[index]];
});


var options = document.querySelectorAll('.goal_name input[type="checkbox"]');
var selectedCount = 0;
var firstSelectedIndex = -1;
var selectedIndex = [-1, -1];

document.addEventListener('DOMContentLoaded', function() {
  options.forEach(function(checkbox) {
    checkbox.checked = false;
  });

  options.forEach(function(checkbox, index) {
    checkbox.addEventListener('change', function() {
      var parent = this.closest('.goal_option');
      if (this.checked) {
        if (selectedCount < 2) {
          parent.classList.add('selected');
          selectedCount++;
          if (selectedCount === 1) {
            firstSelectedIndex = index;
            selectedIndex[0] = index;
          }
          if (selectedCount === 2) {
            selectedIndex[1] = index;
          }
        } else {
          // Deselect the first selected option
          options[firstSelectedIndex].checked = false;
          var firstSelectedParent = options[firstSelectedIndex].closest('.goal_option');
          firstSelectedParent.classList.remove('selected');
          // Select the newly clicked option
          this.checked = true;
          parent.classList.add('selected');
          // Update the first selected index
          firstSelectedIndex = selectedIndex[1];
          selectedIndex[0] = selectedIndex[1];
          selectedIndex[1] = index;
        }
      } else {
        parent.classList.remove('selected');
        selectedCount--;
        if (index === selectedIndex[0]) {
          // Update the first selected index with the second selected index
          firstSelectedIndex = selectedIndex[1];
          selectedIndex[0] = selectedIndex[1];
          selectedIndex[1] = -1;
        }
      }
    });
  });

  var goalOptions = document.querySelectorAll('.goal_option');
  goalOptions.forEach(function(option) {
    option.addEventListener('click', function() {
      var checkboxBtn = option.querySelector('input[type="checkbox"]');
      if (checkboxBtn) {
        checkboxBtn.checked = !checkboxBtn.checked;
        checkboxBtn.dispatchEvent(new Event('change'));
      }
    });
  });
});
