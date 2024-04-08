# Создайте модель Автор. Модель должна содержать следующие поля:
# ○ имя до 100 символов
# ○ фамилия до 100 символов
# ○ почта
# ○ биография
# ○ день рождения
# Дополнительно создай пользовательское поле “полное
# имя”, которое возвращает имя и фамилию.
# Создайте модель Статья (публикация). Авторы из прошлой задачи могут писать статьи.
# У статьи может быть только один автор. У статьи должны быть следующие обязательные поля:
# >>> заголовок статьи с максимальной длиной 200 символов
# ○ содержание статьи
# ○ дата публикации статьи
# ○ автор статьи с удалением связанных объектов при удалении автора
# ○ категория статьи с максимальной длиной 100 символов
# ○ количество просмотров статьи со значением по умолчанию 0
# ○ флаг, указывающий, опубликована ли статья со значением по умолчанию False
# Создайте модель Комментарий.
# Авторы могут добавлять комментарии к своим и чужим статьям. Т.е. у комментария может быть один автор.
# И комментарий относится к одной статье. У модели должны быть следующие поля
# ○ автор
# ○ статья
# ○ комментарий
# ○ дата создания
# ○ дата изменения
# Создайте шаблон для вывода всех статей автора в виде списка заголовков.
# ○ Если статья опубликована, заголовок должен быть ссылкой на статью.
# ○ Если не опубликована, без ссылки.
# Не забываем про код представления с запросом к базе данных и маршруты.
# Продолжаем работу с авторами, статьями и комментариями. Создайте форму для добавления нового автора в базу данных.
# Используйте ранее созданную модель Author
#

import random
from django.shortcuts import render
from .models import Author, Article, Comment
from .forms import AuthorForm

import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    context = {
        'title': 'Home Page',
        'message': 'Welcome to the Home page!'
    }
    return render(request, 'base.html', context)


def author_form(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            biography = form.cleaned_data['biography']
            date_of_birth = form.cleaned_data['date_of_birth']
            author = Author(name=name, surname=surname, email=email, biography=biography, date_of_birth=date_of_birth)
            author.save()
            logger.info(f'Author {name} {surname} saved to database!')
            message = 'New author was successfully added!\nFill out the form to add a new author'
            return render(request, 'articles_app/author_form.html', {'form': form,
                                                                     'message': message})
        else:
            message = 'Invalid data'
    else:
        form = AuthorForm()
        message = 'Fill out the form to add a new author'
    return render(request, 'articles_app/author_form.html', {'form': form,
                                                             'message': message})
