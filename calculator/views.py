import django
from django.shortcuts import render
from django.urls import reverse

DATA = {
    'Омлет': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'Макароны': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'Бутерброд': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def show_recipe(request, dish: dict) -> django.http.response.HttpResponse:  # передаем название блюда и число порций
    """
    Функция получает словарь с данными текущего блюда, вычисляет ингридиенты исходя из числа порций
    Создает новый словарь с результатирующим рецептом блюда, выдает в браузер
    В браузере набрать
    http://127.0.0.1:8000/show/omlet/ 1 порция
    http://127.0.0.1:8000/show/omlet/?servings=2 - 2 порции
    """
    rec = DATA.get(dish)  # получаем словарь с данными текущего блюда
    pics = int(request.GET.get('servings', 1))  # По умолчанию 1 порция

    rec1 = {}  # словарь для подготовки рецепта с нужным числом порций
    for key, value in rec.items():
        rec1[key] = round(value * pics, 2)
    context = {
        'product': dish,  # название блюда
        'recipe': rec1,  # рецепт
        }
    print('context', context)

    return render(request, 'calculator/index.html', context)


def menu(request):
    return render(request, 'menu.html')
