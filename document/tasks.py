from django.core.mail import send_mail
from django.conf import settings
from users.models import User
from celery import shared_task

domain = '"http://localhost:8000/'


@shared_task(serializer="pickle")
def send_mail_to_admin(document, document_id, user):
    admin = User.objects.filter(is_staff=True)
    send_mail(
        subject=f'{user} отправил документы для подтвержедения',
        message=f"""
        Документ для подтверждения - {domain}{document.url},
        Ссылка для подтверждения -  {domain}verificated/{document_id}/'
        """,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=admin
    )


@shared_task(serializer="pickle")
def send_mail_verification(user):
    send_mail(
        subject='Результат верификации',
        message=f'Ваши документы подтверждены',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user, ]
    )


@shared_task(serializer="pickle")
def send_mail_not_verified(user):
    send_mail(
        subject='Резульатат верификации',
        message='Ваши документы не подтврждены, загрузите документы повторно',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user, ]
    )
