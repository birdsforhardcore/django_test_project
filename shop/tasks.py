from conf.celery import background_task
from .service import send
from .models import Mail
from django.core.mail import send_mail


@background_task.task
def send_msg_to_email(user_email):
    """Запуск в фоне"""
    send(user_email)


@background_task.task
def send_spam():
    """Запуск задач по расписанию"""
    users = Mail.objects.all()
    for user in users:
        send_mail(
            'Заголовок сообщения',
            'Текст сообщения',
            'test_project@gmail.com',
            [user.mail],
            fail_silently=False
        )
