from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.urls import reverse

tanks = 'TN'
healer = 'HL'
dd = 'DD'
trader = 'MH'
guildmasters = 'GM'
questgivers = 'QG'
blacksmiths = 'BM'
leatherworker = 'LW'
alchemist = 'AL'
spellmasters = 'SM'

categories = [
    ('tank', 'Танк'),
    ('healer', 'Хил'),
    ('dd', 'ДД'),
    ('trader', 'Торговец'),
    ('guildmaster', 'Гилдмастер'),
    ('questgiver', 'Квестгивер'),
    ('blacksmith', 'Кузнец'),
    ('leatherworker', 'Кожевник'),
    ('alchemist', 'Зельевар'),
    ('spellmaster', 'Мастер заклинаний'),
]


class Author(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_name}'


class Category(models.Model):

    name_category = models.CharField(max_length=20, choices=categories, default='category name')

    def __str__(self):
        return f'{self.name_category}'


class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=categories)
    date_create = models.DateTimeField(auto_now_add=True)
    content = models.FileField(upload_to='content/', blank=True)


def __str__(self):
    return self.title


def get_absolute_url(self):
    return reverse('ad', args=[str(self.id)])


class Responses(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='response')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    accept = models.BooleanField(default=False)

    def __str__(self):
        return self.text[:20] + '...'

    def accepted(self):
        self.accept = True
        self.save()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class CategorySubscribe(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Категории подписчиков'

    def __str__(self):
        return f'{self.category}: {self.subscriber}'
