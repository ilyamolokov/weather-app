from django.http import Http404
import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import City
from .forms import CityForm
from django.utils.text import slugify
import random, string

# Create your views here.

def weather_list(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang=ru&appid=be11199a30cca179654909b1d5c364a8'

    city_weather_data = []
    cities = City.objects.all()
    for city in cities:
        res = requests.get(url.format(city)).json()
        if res['cod'] == "404":
            city.delete()
        else:
            city_weather = {
                'slug': city.slug,
                'name': res['name'],
                'rus_name': city.rus_name,
                'temperature': res['main']['temp'],
                'pressure': res['main']['pressure'],
                'condition': res['weather'][0]['description'],
                'temp_min':res['main']['temp_min'],
                'temp_max':res['main']['temp_max'],
                'icon': res['weather'][0]['icon'],
                'wind': res['wind']['speed'],
                'humidity':res['main']['humidity'],
            }
            city_weather_data.append(city_weather)
    if len(city_weather_data) <= 5:
        context = {'city_weather_data': city_weather_data}
        return render(request, 'weather/weather_list.html', context)
    elif len(city_weather_data) > 5:
        list_length = len(city_weather_data) - 5
        for i in range(list_length):
            del city_weather_data[-1]
        context = {'city_weather_data': city_weather_data}
        return render(request, 'weather/weather_list.html', context)

def weather_detail(request, slug=None):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang=ru&appid=be11199a30cca179654909b1d5c364a8'

    city = get_object_or_404(City, slug=slug)

    res = requests.get(url.format(city)).json()
    if res['cod'] == "404":
        return redirect('weather:weather_list')
    else:
        city_weather_data = {
            'slug': city.slug,
            'name': res['name'],
            'rus_name': city.rus_name,
            'temperature': res['main']['temp'],
            'condition': res['weather'][0]['description'],
            'temp_min':res['main']['temp_min'],
            'temp_max':res['main']['temp_max'],
            'icon': res['weather'][0]['icon'],
            'wind': res['wind']['speed'],
            'humidity':res['main']['humidity'],
        }
    context = {'city_weather_data':city_weather_data}
    return render(request, 'weather/weather_detail.html', context)


def city_delete(request, slug=None):
    city = get_object_or_404(City, slug=slug)
    city.delete()
    return redirect('weather:weather_list')

def city_create(request):
    queryset = City.objects.all()
    if request.method == "POST":
        form = CityForm(request.POST or None)
        if form.is_valid():
            city = form.save(commit=False)
            curr_city = City.objects.filter(slug__icontains=slugify(city.name))
            if curr_city.exists():
                city.slug=slugify(city.name)+"-"+str(random.randint(1000,10000))+str(''.join(random.choice(string.ascii_lowercase) for i in range(6)))
                city.save()
            else:
                city.save()
            return redirect(city.get_absolute_url())
    else:
        form = CityForm()
        context = {'form' : form}
    return render(request, 'weather/city_create.html', context)

def city_edit(request, slug=None):
    queryset = City.objects.all()
    city = get_object_or_404(City, slug=slug)
    if request.method == "POST":
        form = CityForm(request.POST or None, instance=city)
        if form.is_valid():
            city = form.save(commit=False)
            curr_city = City.objects.filter(slug__icontains=slugify(city.name))
            if curr_city.exists():
                city.slug=slugify(city.name)+"-"+str(random.randint(1000,10000))+str(''.join(random.choice(string.ascii_lowercase) for i in range(6)))
                city.save()
            else:
                city.slug=slugify(city.name)
                city.save()
            return redirect(city.get_absolute_url())
    else:
        form = CityForm(instance=city)
        context = {'form' : form}
    return render(request, 'weather/city_edit.html', context)
