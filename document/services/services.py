from django.core.mail import send_mail
from django.conf import settings
from users.models import User

domain = '"http://localhost:8000/'


def send_mail_to_admin(document, document_id, user):
    admin = User.objects.filter(is_staff=True)
    print(admin)
    print(user)
    print(document)
    send_mail(
        subject=f'{user} отправил документы для подтвержедения',
        message=f"""
        Документ для подтверждения - {domain}{document.url},
        Ссылка для подтверждения -  {domain}verificated/{document_id}/'
        """,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=admin
    )
    print("отправлено")


def send_mail_verification(user):
    send_mail(
        subject='Результат верификации',
        message=f'Ваши документы подтверждены',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user,]
    )
    print('Сообщение отправлено')


def send_mail_not_verified(user):
    send_mail(
        subject='Резульатат верификации',
        message='Ваши документы не подтврждены, загрузите документы повторно',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user,]
    )
    print('Сообщение отправлено')
