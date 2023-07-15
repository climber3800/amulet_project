const prices = {
  Silver: "79.99$",
  Steel: "44.99$",
  Wood: "14.99$",
};

const material_description = {
  Silver: "Silver possesses a subtle and enchanting beauty, making it a popular choice for runic amulets. It is associated with the moon, intuition, and feminine energy. Silver is known for its reflective properties, symbolizing clarity, protection, and emotional balance. When worn as an amulet, silver is believed to enhance intuition, foster emotional healing, and promote a deeper connection with the spiritual realm.",
  Steel: "Steel represents strength, resilience, and protection. It possesses a modern and industrial aesthetic, symbolizing endurance and fortitude. Stainless steel amulets are believed to provide a shield against negative energies, instill confidence, and promote a sense of inner strength. They are a reminder of the wearer's ability to overcome challenges and embrace their own power with unwavering determination.",
  Wood: "The natural warmth and grounding energy of wood make it a compelling material for runic amulets. Wood represents growth, stability, and harmony with nature. It embodies the energy of the earth, grounding the wearer and providing a sense of balance and resilience. Wooden amulets are believed to encourage personal growth, foster a deep connection with the natural world, and promote a sense of inner peace and stability."
};
//Gold: "The allure of gold lies not only in its radiant beauty but also in its symbolic significance. As a material for runic amulets, gold represents wealth, abundance, and prosperity. It carries the energy of the sun, bringing warmth and vitality to the wearer. Gold is believed to enhance confidence, attract success, and empower the owner with a sense of self-worth and inner strength.",


var price = document.querySelectorAll('.price');
var description = document.querySelectorAll('.material_description');

function keys(obj) {
    return Object.keys(obj);
};

var symbolKeys = keys(prices);
var descriptionKeys = keys(material_description);

price.forEach(function(symbol, index) {
    symbol.textContent = prices[symbolKeys[index]];
});

description.forEach(function(symbol, index) {
    symbol.textContent = material_description[descriptionKeys[index]];
});



// card movements
var materialOptions = document.querySelectorAll('.material-option');

materialOptions.forEach(function(option) {
  option.addEventListener('click', function() {
    materialOptions.forEach(function(otherOption) {
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