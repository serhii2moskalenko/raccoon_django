from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

menu=[
    'Про навчання',
    'Про нас',
    'Фото',
    'Ціни',
    'Контакти'
]
def index(request):
    context = {
        'title': 'Main page',
        'menu': menu,
    }
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html', {'title': 'About page'})


def categories(request, category_id):
    return HttpResponse(f"<h1>Articles by category</h1><p>id: {category_id}</p>")


def categories_by_slug(request, category_slug):
    return HttpResponse(f"<h1>Articles by category</h1><p>slug: {category_slug}</p>")


def archive(request, year):
    """
    A function that generates an HttpResponse containing information about articles by year.

    Parameters:
    - request: HttpRequest object
    - year: int, the year
    return HttpResponse(f"<h1>Archive</h1><p>year: {year}</p>")
    """

    return HttpResponse(f"<h1>Archive</h1><p>year: {year}</p>")
