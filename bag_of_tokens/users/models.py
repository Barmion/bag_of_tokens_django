from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    email = models.EmailField(
        verbose_name='Электронная почта',
        blank=True)
    telegram_id = models.CharField(
        verbose_name='Телеграм id',
        max_length=20,
        unique=True,
    )
    is_telegram_bot = models.BooleanField(
        verbose_name='Это телеграм бот?',
        default=False
    )

    REQUIRED_FIELDS = [
        'telegram_id',
    ]

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
