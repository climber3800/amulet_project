import os
from django.conf import settings
from PIL import Image

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "amulet.settings")

runes = ["Fehu", "Uruz", "Thurisaz", "Ansuz", "Raidho", "Kenaz", "Gebo", "Wunjo", "Hagalaz", "Naudhiz", "Isa", "Jera", "Eihwaz",
         "Perthro", "Algiz", "Sowilo", "Tiwaz", "Berkana", "Ehwaz", "Mannaz", "Laguz", "Ingwaz", "Dagaz", "Othala"]

goal_rune_combinations = {
    "career_advancement": ["Dagaz", "Ansuz", "Tiwaz", "Kenaz", "Ingwaz"],
    "financial_stability": ["Fehu", "Jera", "Raidho", "Wunjo", "Othala"],
    "educational_achievement": ["Algiz", "Gebo", "Sowilo", "Raidho", "Ansuz"],
    "personal_growth": ["Berkana", "Ehwaz", "Mannaz", "Ingwaz", "Dagaz"],
    "healthy_lifestyle": ["Eihwaz", "Perthro", "Sowilo", "Uruz", "Algiz"],
    "strong_relationships": ["Gebo", "Kenaz", "Mannaz", "Raidho", "Wunjo"],
    "life_partner": ["Gebo", "Ehwaz", "Jera", "Raidho", "Wunjo"],
    "travel_exploration": ["Ehwaz", "Raidho", "Ansuz", "Jera", "Dagaz"],
    "owning_home": ["Othala", "Fehu", "Ingwaz", "Perthro", "Jera"],
    "starting_family": ["Ingwaz", "Berkana", "Naudhiz", "Jera", "Ehwaz"],
    "independent_life": ["Kenaz", "Mannaz", "Gebo", "Ingwaz", "Othala"],
    "social_boundaries": ["Algiz", "Ehwaz", "Raidho", "Jera", "Dagaz"],
    "overcoming_fears": ["Algiz", "Tiwaz", "Eihwaz", "Ansuz", "Dagaz"],
    "mindfulness_inner_peace": ["Isa", "Gebo", "Ansuz", "Mannaz", "Dagaz"],
    "positive_impact": ["Kenaz", "Gebo", "Mannaz", "Ingwaz", "Wunjo"],
    "pursuing_passion": ["Kenaz", "Ansuz", "Ehwaz", "Berkana", "Dagaz"],
    "mental_wellbeing": ["Gebo", "Eihwaz", "Raidho", "Sowilo", "Dagaz"],
    "closertoGod": ["Ansuz", "Kenaz", "Mannaz", "Jera", "Ingwaz"],
    "sustainable_lifestyle": ["Othala", "Ingwaz", "Algiz", "Berkana", "Jera"],
    "purpose_meaning": ["Ansuz", "Kenaz", "Mannaz", "Dagaz", "Othala"]}

horoscope_runes = {
    "Aries": ["Tiwaz", "Algiz", "Fehu"],
    "Taurus": ["Uruz", "Berkana", "Hagalaz"],
    "Gemini": ["Ansuz", "Kenaz", "Gebo"],
    "Cancer": ["Raidho", "Jera", "Laguz"],
    "Leo": ["Sowilo", "Mannaz", "Wunjo"],
    "Virgo": ["Kenaz", "Ingwaz", "Perthro"],
    "Libra": ["Gebo", "Algiz", "Ehwaz"],
    "Scorpio": ["Naudhiz", "Hagalaz", "Perthro"],
    "Sagittarius": ["Tiwaz", "Eihwaz", "Jera"],
    "Capricorn": ["Tiwaz", "Isa", "Othala"],
    "Aquarius": ["Ansuz", "Dagaz", "Ehwaz"],
    "Pisces": ["Algiz", "Raidho", "Ingwaz"]
}

rune_combinations = {
    "Protection": ["Algiz", "Thurisaz", "Isa"],
    "Strength": ["Tiwaz", "Uruz", "Sowilo"],
    "Courage": ["Tiwaz", "Naudhiz", "Eihwaz"],
    "Wisdom": ["Ansuz", "Eihwaz", "Raidho"],
    "Prosperity": ["Fehu", "Jera", "Ingwaz"],
    "Health": ["Jera", "Sowilo", "Ehwaz"],
    "Love": ["Gebo", "Wunjo", "Kenaz"],
    "Peace": ["Algiz", "Gebo", "Dagaz"]}

rune_alphabet = {"A": "Ansuz", "B": "Berkana", "C": "Kenaz", "D": "Dagaz", "E": "Eihwaz", "F": "Fehu", "G": "Gebo",
                 "H": "Hagalaz", "I": "Isa", "J": "Jera", "K": "Kenaz", "L": "Laguz", "M": "Mannaz", "N": "Naudhiz",
                 "O": "Othala", "P": "Perthro", "Q": "Kenaz", "R": "Raidho", "S": "Sowilo", "T": "Tiwaz", "U": "Uruz",
                 "V": "Wunjo", "W": "Wunjo", "X": "Gebo", "Y": "Algiz", "Z": "Eihwaz"}

rotation = [0, -15, -30, -45, -60, -75, -90, -105, -120, -135, -150, -165, -180, -195, -210, -225, -240, -255, -270, -285, -300, -315, -330, -345]
positions = [(530, 20), (661, 38), (784, 89), (890, 170), (971, 275), (1022, 399), (1040, 530), (1022, 661), (971, 784), (890, 890), (785, 971), (661, 1022), (530, 1040), (399, 1022), (276, 971), (170, 890), (89, 785), (38, 661), (20, 530), (38, 399), (89, 276), (170, 170), (275, 89), (399, 38)]


def combine_horoscope(received_horoscope):
    return horoscope_runes[received_horoscope]


def combine_goals(received_goals):
    ten_runes = []
    for n in received_goals:
        ten_runes += goal_rune_combinations[n]
    return ten_runes


def combine_qualities(received_qualities):
    nine_runes = []
    for n in received_qualities:
        nine_runes += rune_combinations[n]
    return nine_runes


def combine_name(received_name, received_last_name):
    runes_from_name_letters = []
    first = received_name[0].upper()
    second = received_last_name[0].upper()
    if first in rune_alphabet:
        runes_from_name_letters.append((rune_alphabet[first]))
    if second in rune_alphabet:
        runes_from_name_letters.append((rune_alphabet[second]))
    return runes_from_name_letters


def change_image(style, runes):
    if style is not None:
        silver_background = Image.open(os.path.join(settings.STATIC_ROOT, 'images/amulet_style/silver/' + style + '.png'))
        steel_background = Image.open(os.path.join(settings.STATIC_ROOT, 'images/amulet_style/steel/' + style + '.png'))
        wood_background = Image.open(os.path.join(settings.STATIC_ROOT, 'images/amulet_style/wood/' + style + '.png'))

        opened_runes = []
        for n in runes:
            opened_runes.append(Image.open(os.path.join(settings.STATIC_ROOT, 'images/runes/' + n + '.png')))

        for i in range(len(positions)):
            rotated_rune = opened_runes[i].rotate(rotation[i], expand=False)
            steel_background.paste(rotated_rune, positions[i], mask=rotated_rune)
            silver_background.paste(rotated_rune, positions[i], mask=rotated_rune)
            wood_background.paste(rotated_rune, positions[i], mask=rotated_rune)

        return silver_background, steel_background, wood_background
