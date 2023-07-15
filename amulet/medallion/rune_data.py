symbolsDictionary = {
    "Yggdrasil": "The Yggdrasil symbol, represents the World Tree in Norse mythology, embodies the interconnectedness of all things and the cyclical nature of life. Including the Yggdrasil on your personalized runic amulet signifies a deep connection to the natural world, spiritual growth, and a reminder of the infinite possibilities for renewal and transformation.",
    "Vegvisir": "The Vegvisir, known as the Viking Compass, is a symbol of guidance and protection, helping one find their way through life's challenges. Including the Vegvisir on your personalized runic amulet signifies a desire for clarity, inner strength, and the ability to navigate through difficult times with steadfastness and purpose.",
    "Valknut": "The Valknut represents the connection between life, death, and the eternal cycle of existence. Including the Valknut on your personalized runic amulet signifies bravery, the pursuit of knowledge, and a deep connection to the divine, serving as a symbol of protection and guidance on your spiritual journey.",
    "Aegishjalmur": "Aegishjalmur, also known as the Helm of Awe, is a powerful symbol of protection, strength, and invincibility in Norse mythology. Including the Ægishjálmur on your personalized runic amulet signifies a shield against negativity, fearlessness in the face of challenges, and the ability to tap into your inner courage and resilience. It serves as a potent talisman to empower and safeguard you on your journey.",
    "Astarstafur": "The Aðstafur, also known as the Icelandic Love Stave, is a symbol associated with love, attraction, and romance. Including the Aðstafur on your personalized runic amulet signifies a desire for love, emotional connection, and harmonious relationships. It serves as a potent symbol to enhance the energy of love in your life and foster a deeper sense of connection with others.",
    "Baenarstafur": "The Baenarstafur, also known as the Icelandic Sorcerer's Compass, is a symbol associated with banishing and protection against negative energies and influences. Including the Baenarstafur on your personalized runic amulet signifies a strong defense against harmful forces, the ability to dispel negativity, and the maintenance of a sacred and safe space.",
    "Troll cross": "The Troll Cross is believed to ward off evil spirits and protect against malevolent forces. Great powers are attributed to this symbol as it is not only able to help humans, but also to help animals, personal property, constructions and buildings.",
    "Danobus": "Including the Danobus symbol on your personalized runic amulet signifies a deep intention to manifest your wishes and align with the forces of the universe to bring about your desired outcomes. It serves as a symbol of manifestation, intention-setting, and a reminder to actively participate in the co-creation of your reality.",
    "Draumstafir": "Draumstafir, also known as Dream Staves, are symbols associated with dreams, protection, and divination in Icelandic folklore. Including it on your personalized runic amulet signifies a connection to the realm of dreams and the ability to receive insights and guidance during sleep. It serves as a powerful symbol for spiritual exploration, and unlocking the mysteries of the subconscious mind.",
    "Hagall Hinn Minni": "The Hagall Hinn Minni symbol is a powerful stave renowned for its protective qualities against magic. Carry it with you as a potent talisman, and embrace its shielding energy, offering you reassurance and protection and the effects of others' magic and charms. Feel confident and secure knowing that you are safeguarded from external enchantments.",
    "Karlmennsku": "Karlmennsku is a symbol that serves to amplify and enhance masculine energies, available for use by anyone. When incorporated into a personalized runic amulet, it works to magnify leadership qualities, assertiveness, courage, endurance, and physical strength, empowering individuals with a heightened sense of masculine attributes and attributes associated with them.",
    "Kaupaloki": "Kaupaloki is a Viking symbol associated with business and prosperity, was used as a talisman to enhance commercial ventures, protect against negative influences, and safeguard against fraudulent activities. Using this symbol, you invite the energies of success, prosperity, and integrity into your business endeavors, ensuring smooth transactions and shielding yourself from malicious intentions and gossip.",
    "Lukkustafir": "Lukkustafir, also known as Icelandic Magical Staves of Locking, is a symbol associated with protection, sealing, and securing. Lukkustafir serves as a powerful symbol of safeguarding, warding off negative energies, and creating a shield of defense. It symbolizes the ability to lock away or prevent unwanted influences, allowing you to maintain a sense of security and control in your life.",
    "Lygistafir": "Lygistafir is a potent runic symbol known for its ability to compel truth-telling. When incorporated into your personalized runic amulet, it harnesses the power to influence others to speak honestly and reveal the truth. It serves as a tool to foster transparency, uncover hidden information, and promote truthful communication in various situations.",
    "Ottasafur": "Ottasafur possesses the power to shield the wearer and evoke fear in adversaries during battle. In contemporary usage, it finds relevance in competitions, serving as a conduit for its potent magic. By wearing Ottasafur on your personalized runic amulet, you tap into its formidable energy, providing protection and a formidable presence in various endeavors.",
    "The Horned Triskel": "The Horned Triskel represents a connection to nature, strength, and spiritual energy. It embodies the power of the wild and serves as a symbol of vitality, transformation, and the cyclical nature of life. Including The Horned Triskel on your amulet signifies a deep connection to the primal forces, a celebration of life's cycles, and the pursuit of personal growth and empowerment.",
    "Tyngfinder": "Tyngfinder is utilized for locating lost objects and belongings. To activate its effect, the user wears it and places it under their head while sleeping, allowing it to guide them through a revealing dream. By incorporating Tyngfinder into your personalized runic amulet, you harness its ability to assist in finding lost items, providing a connection to the subconscious realm and unlocking hidden knowledge.",
    "Ygrgugnir": "Ygrgugnir, as the spear of the god Odin, represents strength and power. Its name evokes a sense of violent tremor, symbolizing its formidable impact. Including Ygrgugnir on your personalized runic amulet signifies a connection to the strength of Odin, invoking courage, resilience, and the ability to overcome challenges with unwavering force.",
}

goals_dict = {
    "career_advancement": "Career Advancement",
    "financial_stability": "Financial Stability",
    "educational_achievement": "Educational Achievement",
    "personal_growth": "Personal Growth and Development",
    "healthy_lifestyle": "Healthy Lifestyle and Fitness",
    "strong_relationships": "Building Strong Relationships",
    "life_partner": "Finding a Life Partner",
    "travel_exploration": "Travel and Exploration",
    "owning_home": "Owning Material Possessions",
    "starting_family": "Starting a Family",
    "independent_life": "Having an Independent Life",
    "social_boundaries": "Being Free of Social Boundaries",
    "overcoming_fears": "Overcoming Fears and Limiting Beliefs",
    "mindfulness_inner_peace": "Cultivating Mindfulness and Inner Peace",
    "positive_impact": "Making a Positive Impact on Others",
    "pursuing_passion": "Pursuing a Passion or Hobby",
    "mental_wellbeing": "Enhancing Mental Well-being",
    "closertoGod": "Growing Closer to God",
    "sustainable_lifestyle": "Living a Sustainable and Eco-friendly Lifestyle",
    "purpose_meaning": "Finding Purpose and Meaning in Life"
}


def center_symbol_description(style):
    if style in symbolsDictionary:
        return symbolsDictionary[style]
    else:
        return None


def name_clean(name):
    if name is not None and len(name) == 2:
        return name[0] + ' and ' + name[1]
    else:
        return 'Name not available'


def horoscope_clean(horoscope):
    if horoscope is not None and len(horoscope) == 3:
        return horoscope[0] + ', ' + horoscope[1] + ' and ' + horoscope[2]
    else:
        return 'Horoscope sign not available'


def qualities_clean(qualities, runes):
    if qualities is not None and len(qualities) == 3 and runes is not None and len(runes) == 9:
        return f"{qualities[0]} is represented with {runes[0]}, {runes[1]} and {runes[2]}, {qualities[1]} with {runes[3]}, {runes[4]}, {runes[5]} and {qualities[2]} with {runes[6]}, {runes[7]} and {runes[8]}"
    else:
        return 'Qualities not available'

def goals_clean(goals, runes):
    if goals is not None and len(goals) == 2 and runes is not None and len(runes) == 10:
        return f"The first your goal ({goals_dict[goals[0]]}) is represented with these five runes - {runes[0]}, {runes[1]}, {runes[2]}, {runes[3]} and {runes[4]}. Your second goal ({goals_dict[goals[1]]}) is represented with - {runes[5]}, {runes[6]}, {runes[7]}, {runes[8]} and {runes[9]}."
    else:
        return 'Goals not avaliable'