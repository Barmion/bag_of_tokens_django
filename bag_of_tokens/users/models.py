from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    email = models.EmailField(
        verbose_name='Электронная почта',
        blank=True,
        unique=True)
    telegram_id = models.CharField(
        verbose_name='Телеграм id',
        blank=True,
        default='',
        max_length=20
    )
    is_telegram_bot = models.BooleanField(
        verbose_name='Это телеграм бот?',
        default=False
    )

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'Пользователи'
