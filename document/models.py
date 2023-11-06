from django.db import models
from users.models import User
from django.conf import settings

NULLABLE = {'blank': True, 'null': True}


class Document(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    verification_status = models.BooleanField(default=False, verbose_name='cтатус верификации')
    document = models.ImageField(**NULLABLE, verbose_name='документ подтверждающий личность')

    class Meta:
        verbose_name = 'документ'
        verbose_name_plural = 'документы'