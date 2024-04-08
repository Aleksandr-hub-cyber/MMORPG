from celery import shared_task
from datetime import timedelta
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Category, Author, Post, PostCategory, Comment, CategorySubscribe


@shared_task
def monday():
    some_day_last_week = timezone.now().date() - timedelta(days=7)
    post = Post.objects.filter(created__gt=some_day_last_week)
    user = CategorySubscribe.objects.all()
    user_list = []
    for u in user:
        if u.user not in user_list:
            user_list.append(u.user)
    for u in user_list:
        news_list = []
        for p in post:
            cats = Post.get_category_id(p)
            for c in cats:
                if CategorySubscribe.objects.filter(cats_id=c, user_id=u.pk):
                    if p.title not in news_list:
                        news_list.append(p.title)

        email = User.objects.get(pk=u.pk)
        em=[]
        em.append(email.email)
        send_mail(
            subject='Новая новость!',
            message="\n ".join(news_list),
            from_email='123user123@yandex.by',
            recipient_list=em
        )


@shared_task
def email_add_post(title, text, email):
    for x in email:
        em=[]
        em.append(x)
        user = User.objects.get(email=x)
        send_mail(
            subject=title,
            message=f'Здравствуйте, у нас появилась новая новость.\n{text[:50]}',
            from_email='123user123@yandex.by',
            recipient_list=em
        )