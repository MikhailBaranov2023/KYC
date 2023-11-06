from django.core.mail import send_mail
from django.conf import settings
from users.models import User


def send_mail_to_admin(document, user):
    admin = User.objects.filter(is_staff=True)
    print(admin)
    print(user)
    send_mail(
        subject=f'{user} отправил документы для подтвержедения',
        message=document,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=admin
    )
    print("отправлено")
