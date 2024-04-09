from django.db.models.signals import post_save
from django.core.mail import send_mail
from .models import Responses, CategorySubscribe
from django.dispatch import receiver


@receiver(post_save, sender=Responses)
def notify_user_subscribe(sender, instance, created, **kwargs):
    if created:
        subject = f'Новый отклик'
    else:
        subject = f'Ваш отклик одобрен'

    send_mail(
        subject=subject,
        message=f'Вам оставлен новый отклик: {instance.text_responses}',
        from_email='win.c4ester@yandex.ru',
        recipient_list=[f'{instance.responses_comment.author_name.email}'],
    )


#
def notify_user_subscribe(sender, instance, created, **kwargs):
    subject = f'Новый публикация'
    send_mail(
        subject=subject,
        message=f'Новая публикая в разделе: {instance.header}',
        from_email='win.c4ester@yandex.ru',
        recipient_list=[f'{instance.author_name.email}'],
    )


@receiver(post_save, sender=CategorySubscribe)
def notify_user_subscribe(sender, instance, created, **kwargs):
    subject = f'Подписка оформлена'
    send_mail(
        subject=subject,
        message=f'Вы успешно подписались на категорию: {instance.category.name_category}',
        from_email='win.c4ester@yandex.ru',
        recipient_list=[f'{instance.subscriber.email}'])
