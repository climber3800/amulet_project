from django.shortcuts import render, redirect
from io import BytesIO
import base64
from medallion.models import UserAmulet
from medallion import forms
from medallion.amulet_program import combine_qualities, combine_name,\
    change_image, combine_horoscope, combine_goals
from medallion.rune_data import center_symbol_description, name_clean, horoscope_clean, qualities_clean, goals_clean


def runes_func(request):
    return render(request, 'runes/runes_main_page.html')


def rune_create_design(request):
    form = forms.RuneAttributes()

    if request.method == "POST":
        form = forms.RuneAttributes(request.POST)

        if form.is_valid():
            style = form.cleaned_data['design']
            request.session['style'] = style

            if 'next' in request.POST:
                return redirect('amulet:rune_create_name')
        else:
            return redirect('amulet:rune_create_design')

    return render(request, 'runes/rune_creation.html', {'form': form})


def rune_create_name(request):
    form = forms.RuneName()

    if request.method == "POST":
        form = forms.RuneName(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            request.session['name'] = name
            last_name = form.cleaned_data['last_name']
            request.session['last_name'] = last_name
            horoscope = form.cleaned_data['horoscope']
            request.session['horoscope'] = horoscope

            result_from_name = combine_name(name, last_name)
            request.session['result_from_name'] = result_from_name

            result_from_horoscope = combine_horoscope(horoscope)
            request.session['result_from_horoscope'] = result_from_horoscope

            if 'next2' in request.POST:
                return redirect('amulet:rune_qualities')

    return render(request, 'runes/rune_creation_two.html', {'form': form})


def rune_qualities(request):
    form = forms.RuneQualities()

    if request.method == "POST":
        form = forms.RuneQualities(request.POST)

        if form.is_valid():
            qualities = form.cleaned_data['qualities']
            if len(qualities) == 3:
                request.session['qualities'] = qualities
                result_from_qualities = combine_qualities(qualities)
                request.session['result_from_qualities'] = result_from_qualities

                if 'next3' in request.POST:
                    return redirect('amulet:rune_goals')
            else:
                form.add_error('qualities', 'Please select exactly 3 qualities.')

    return render(request, 'runes/rune_creation_three.html', {'form': form})


def rune_goals(request):
    form = forms.RuneGoals()

    if request.method == "POST":
        form = forms.RuneGoals(request.POST)

        if form.is_valid():
            goals = form.cleaned_data['goals']
            if len(goals) == 2:
                request.session['goals'] = goals
                result_from_goals = combine_goals(goals)
                request.session['result_from_goals'] = result_from_goals

                # We combine all runes:
                combine_result = []
                combine_result.extend(request.session.get('result_from_name'))
                combine_result.extend(request.session.get('result_from_horoscope'))
                combine_result.extend(request.session.get('result_from_qualities'))
                combine_result.extend(request.session.get('result_from_goals'))
                request.session['combine_result'] = combine_result

                if 'next4' in request.POST:
                    return redirect('amulet:rune_result')
            else:
                form.add_error('goals', 'Please select exactly 2 goals.')

    return render(request, 'runes/rune_creation_four.html', {'form': form})


def rune_result(request):
    style = request.session.get('style')
    description = center_symbol_description(style)
    name_runes = name_clean(request.session.get('result_from_name'))
    name = request.session.get('name')
    last_name = request.session.get('last_name')
    horoscope = request.session.get('horoscope')
    horoscope_runes = horoscope_clean(request.session.get('result_from_horoscope'))
    qualities = qualities_clean(request.session.get('qualities'), request.session.get('result_from_qualities'))
    goals = goals_clean(request.session.get('goals'), request.session.get('result_from_goals'))

    amulet = change_image(style, request.session.get('combine_result'))
    if amulet is not None:
        image_io = BytesIO()
        amulet[1].save(image_io, format='PNG')
        image_base64 = base64.b64encode(image_io.getvalue()).decode('utf-8')
        amulet_src = f"data:image/png;base64,{image_base64}"

        return render(request, 'runes/rune_result.html', {
            'style': style,
            'description': description,
            'name': name,
            'name_runes': name_runes,
            'last_name': last_name,
            'horoscope': horoscope,
            'horoscope_runes': horoscope_runes,
            'qualities': qualities,
            'goals': goals,
            'amulet_src': amulet_src})
    else:
        return redirect('amulet:rune_create_design')


def rune_material(request):
    form = forms.RuneMaterial()

    amulet = change_image(request.session.get('style'), request.session.get('combine_result'))
    if amulet is not None:
        silver_amulet = amulet[0]
        steel_amulet = amulet[1]
        wood_amulet = amulet[2]
        silver_image_io = BytesIO()
        steel_image_io = BytesIO()
        wood_image_io = BytesIO()
        silver_amulet.save(silver_image_io, format='PNG')
        steel_amulet.save(steel_image_io, format='PNG')
        wood_amulet.save(wood_image_io, format='PNG')
        silver_image_base64 = base64.b64encode(silver_image_io.getvalue()).decode('utf-8')
        steel_image_base64 = base64.b64encode(steel_image_io.getvalue()).decode('utf-8')
        wood_image_base64 = base64.b64encode(wood_image_io.getvalue()).decode('utf-8')
        silver_amulet_src = f"data:image/png;base64,{silver_image_base64}"
        steel_amulet_src = f"data:image/png;base64,{steel_image_base64}"
        wood_amulet_src = f"data:image/png;base64,{wood_image_base64}"

        if request.method == "POST":
            form = forms.RuneMaterial(request.POST)

            if form.is_valid():
                material = form.cleaned_data['material']
                request.session['material'] = material

                if 'next5' in request.POST:
                    return redirect('amulet:sorry_page')
            else:
                return redirect('amulet:rune_create_design')

        context = {
            'form': form,
            'silver_amulet_src': silver_amulet_src,
            'steel_amulet_src': steel_amulet_src,
            'wood_amulet_src': wood_amulet_src}

        return render(request, 'runes/rune_matter.html', context)
    else:
        return redirect('amulet:rune_create_design')


def rune_final(request):
    name = request.session.get('name')
    last_name = request.session.get('last_name')
    combine_result = request.session.get('combine_result')
    style = request.session.get('style')
    material = request.session.get('material')

    if not all([name, last_name, combine_result, style, material]):
        return redirect('amulet:rune_create_design')

    try:
        user_amulet = UserAmulet(
            name=name,
            last_name=last_name,
            runes=combine_result,
            style=style,
            material=material
        )
        user_amulet.save()
    except:
        return redirect('amulet:rune_create_design')

    return render(request, 'runes/sorry_page.html')
