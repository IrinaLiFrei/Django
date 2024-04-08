from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    date_of_birth = models.DateField(blank=False)

    def full_name(self):
        return f'{self.name} {self.surname}'

    def __str__(self):
        return f'{self.full_name()} {self.date_of_birth}'


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

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'Article by {self.author} >>> {self.title}'


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} to the article {Article.title} >>> {self.content[:150]}...'
