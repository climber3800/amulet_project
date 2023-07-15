from django import forms
import re


class RuneAttributes(forms.Form):
    IMAGE_CHOICES = (
        ('Yggdrasil', 'Yggdrasil'),
        ('Vegvisir', 'Vegvisir'),
        ('Valknut', 'Valknut'),
        ('Aegishjalmur', 'Aegishjalmur'),
        ('Astarstafur', 'Astarstafur'),
        ('Baenarstafur', 'Baenarstafur'),
        ('Troll cross', 'Troll cross'),
        ('Danobus', 'Danobus'),
        ('Draumstafir', 'Draumstafir'),
        ('Hagall Hinn Minni', 'Hagall Hinn Minni'),
        ('Karlmennsku', 'Karlmennsku'),
        ('Kaupaloki', 'Kaupaloki'),
        ('The Horned Triskel', 'The Horned Triskel'),
        ('Tyngfinder', 'Tyngfinder'),
        ('Ygrgugnir', 'Ygrgugnir'))

    design = forms.ChoiceField(choices=IMAGE_CHOICES, widget=forms.RadioSelect)


class RuneName(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=70, required=True)
    HOROSCOPE_SIGNS = (
        ("Aries", 'Aries'),
        ("Taurus", 'Taurus'),
        ("Gemini", 'Gemini'),
        ("Cancer", 'Cancer'),
        ("Leo", 'Leo'),
        ("Virgo", 'Virgo'),
        ("Libra", 'Libra'),
        ("Scorpio", 'Scorpio'),
        ("Sagittarius", 'Sagittarius'),
        ("Capricorn", 'Capricorn'),
        ("Aquarius", 'Aquarius'),
        ("Pisces", 'Pisces'))

    horoscope = forms.ChoiceField(choices=HOROSCOPE_SIGNS, widget=forms.RadioSelect)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not re.match(r'^[A-Za-z]+$', name):
            raise forms.ValidationError('Only letters are allowed in the Name.')
        return name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not re.match(r'^[A-Za-z]+$', last_name):
            raise forms.ValidationError('Only letters are allowed in the Last name.')
        return last_name


class RuneQualities(forms.Form):
    QUALITY_CHOICES = (
        ('Protection', 'Protection'),
        ('Strength', 'Strength'),
        ('Courage', 'Courage'),
        ('Wisdom', 'Wisdom'),
        ('Prosperity', 'Prosperity'),
        ('Health', 'Health'),
        ('Love', 'Love'),
        ('Peace', 'Peace'))

    qualities = forms.MultipleChoiceField(choices=QUALITY_CHOICES, widget=forms.CheckboxSelectMultiple)


class RuneGoals (forms.Form):
    GOAL_CHOICES = (
        ("career_advancement", "Career Advancement"),
        ("financial_stability", "Financial Stability"),
        ("educational_achievement", "Educational Achievement"),
        ("personal_growth", "Personal Growth and Development"),
        ("healthy_lifestyle", "Healthy Lifestyle and Fitness"),
        ("strong_relationships", "Building Strong Relationships"),
        ("life_partner", "Finding a Life Partner"),
        ("travel_exploration", "Travel and Exploration"),
        ("owning_home", "Owning material possessions"),
        ("starting_family", "Starting a Family"),
        ("independent_life", "Having an independent life"),
        ("social_boundaries", "Being free of social boundaries"),
        ("overcoming_fears", "Overcoming Fears and Limiting Beliefs"),
        ("mindfulness_inner_peace", "Cultivating Mindfulness and Inner Peace"),
        ("positive_impact", "Making a Positive Impact on Others"),
        ("pursuing_passion", "Pursuing a Passion or Hobby"),
        ("mental_wellbeing", "Enhancing Mental Well-being"),
        ("closertoGod", "Growing closer to God"),
        ("sustainable_lifestyle", "Living a Sustainable and Eco-friendly Lifestyle"),
        ("purpose_meaning", "Finding Purpose and Meaning in Life"))

    goals = forms.MultipleChoiceField(choices=GOAL_CHOICES, widget=forms.CheckboxSelectMultiple)


class RuneMaterial(forms.Form):
    MATERIAL_CHOICES = (
        ('Silver', 'Silver'),
        ('Stainless steel', 'Stainless steel'),
        ('Wood', 'Wood'))

    material = forms.ChoiceField(choices=MATERIAL_CHOICES, widget=forms.RadioSelect)
