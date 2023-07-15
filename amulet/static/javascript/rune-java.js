// Add description to cards
const symbolsDictionary = {
  Yggdrasil: "The Yggdrasil symbol, representing the World Tree in Norse mythology, embodies the interconnectedness of all things and the cyclical nature of life. Including the Yggdrasil on your personalized runic amulet signifies a deep connection to the natural world, spiritual growth, and a reminder of the infinite possibilities for renewal and transformation.",
  Vegvisir: "The Vegvisir, known as the Viking Compass, is a symbol of guidance and protection, helping one find their way through life's challenges. Including the Vegvisir on your personalized runic amulet signifies a desire for clarity, inner strength, and the ability to navigate through difficult times with steadfastness and purpose.",
  Valknut: "The Valknut represents the connection between life, death, and the eternal cycle of existence. Including the Valknut on your personalized runic amulet signifies bravery, the pursuit of knowledge, and a deep connection to the divine, serving as a symbol of protection and guidance on your spiritual journey.",
  Aegishjalmur: "Also known as the Helm of Awe, is a powerful symbol of protection, strength, and invincibility in Norse mythology. Including the Ægishjálmur on your personalized runic amulet signifies a shield against negativity, fearlessness in the face of challenges, and the ability to tap into your inner courage and resilience. It serves as a potent talisman to empower and safeguard you on your journey.",
  Astarstafur: "The Aðstafur, also known as the Icelandic Love Stave, is a symbol associated with love, attraction, and romance. Including the Aðstafur on your personalized runic amulet signifies a desire for love, emotional connection, and harmonious relationships. It serves as a potent symbol to enhance the energy of love in your life and foster a deeper sense of connection with others.",
  Baenarstafur: "The Baenarstafur, also known as the Icelandic Sorcerer's Compass, is a symbol associated with banishing and protection against negative energies and influences. Including the Baenarstafur on your personalized runic amulet signifies a strong defense against harmful forces, the ability to dispel negativity, and the maintenance of a sacred and safe space.",
  Trollcross: "The Troll Cross is believed to ward off evil spirits and protect against malevolent forces. Great powers are attributed to this symbol as it is not only able to help humans, but also to help animals, personal property, constructions and buildings.",
  Danobus: "Including the Danobus symbol on your personalized runic amulet signifies a deep intention to manifest your wishes and align with the forces of the universe to bring about your desired outcomes. It serves as a symbol of manifestation, intention-setting, and a reminder to actively participate in the co-creation of your reality.",
  Draumstafir: "Also known as Dream Staves, are symbols associated with dreams, protection, and divination in Icelandic folklore. Including it on your personalized runic amulet signifies a connection to the realm of dreams and the ability to receive insights and guidance during sleep. It serves as a powerful symbol for spiritual exploration, and unlocking the mysteries of the subconscious mind.",
  HagallHinnMinni: "The Hagall Hinn Minni symbol is a powerful stave renowned for its protective qualities against magic. Carry it with you as a potent talisman, and embrace its shielding energy, offering you reassurance and protection from the effects of others' magic and charms. Feel confident and secure knowing that you are safeguarded from external enchantments.",
  Karlmennsku: "Karlmennsku is a symbol that serves to amplify and enhance masculine energies, available for use by anyone. When incorporated into a personalized runic amulet, it works to magnify leadership qualities, assertiveness, courage, endurance, and physical strength, empowering individuals with a heightened sense of masculine attributes and attributes associated with them.",
  Kaupaloki: "a Viking symbol associated with business and prosperity, was used as a talisman to enhance commercial ventures, protect against negative influences, and safeguard against fraudulent activities. Using this symbol, you invite the energies of success, prosperity, and integrity into your business endeavors, ensuring smooth transactions and shielding yourself from malicious intentions and gossip.",
  TheHornedTriskel: "Represents a connection to nature, strength, and spiritual energy. It embodies the power of the wild and serves as a symbol of vitality, transformation, and the cyclical nature of life. Including The Horned Triskel on your amulet signifies a deep connection to the primal forces, a celebration of life's cycles, and the pursuit of personal growth and empowerment.",
  Tyngfinder: "Is utilized for locating lost objects and belongings. To activate its effect, the user wears it and places it under their head while sleeping, allowing it to guide them through a revealing dream. By incorporating Tyngfinder into your personalized runic amulet, you harness its ability to assist in finding lost items, providing a connection to the subconscious realm and unlocking hidden knowledge.",
  Ygrgugnir: "Ygrgugnir, as the spear of the god Odin, represents strength and power. Its name evokes a sense of violent tremor, symbolizing its formidable impact. Including Ygrgugnir on your personalized runic amulet signifies a connection to the strength of Odin, invoking courage, resilience, and the ability to overcome challenges with unwavering force.",
};

var description = document.querySelectorAll('.symbol_description');

function keys(obj) {
    return Object.keys(obj);
};

var symbolKeys = keys(symbolsDictionary);

description.forEach(function(symbol, index) {
    symbol.textContent = symbolsDictionary[symbolKeys[index]];
});


// card movements
var imageOptions = document.querySelectorAll('.image-option');

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









