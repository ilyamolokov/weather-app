from django import forms
from .models import City
from django.core.exceptions import ValidationError

class CityForm(forms.ModelForm):
    name = forms.CharField(label="Название города", max_length=100, widget=forms.TextInput(attrs={"size":36,"placeholder":"Введите название города по-английски", "autocomplete" : "off"}))
    #slug = forms.CharField(label="Friendly URL", required=False, widget=forms.TextInput(attrs={"size":36,"placeholder":"Введите friendly url для этого города", "autocomplete" : "off"}))
    rus_name = forms.CharField(label="Русское название",required=False, widget=forms.TextInput(attrs={"size":36,"placeholder":"Введите название этого города по-русски", "autocomplete" : "off"}))
    class Meta:
        model = City
        fields = ['name', 'rus_name']# 'slug', ]
