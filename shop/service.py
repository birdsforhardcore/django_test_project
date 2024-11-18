from django.core.mail import send_mail
from conf import settings


def send(user_email):
    send_mail(
        subject='Test Project',
        message='Вы подписались на рассылку Test Project',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user_email],
        fail_silently=False,
    )
