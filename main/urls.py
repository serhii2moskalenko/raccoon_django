from django.contrib import admin
from django.urls import path, include, re_path, register_converter

from main import converters
from main.views import index, categories, categories_by_slug, archive, about

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', index),
    path('about/', about),
    path('categories/<int:category_id>/', categories),
    path('categories/<slug:category_slug>/', categories_by_slug),
    path('archive/<year4:year>/', archive),
]
