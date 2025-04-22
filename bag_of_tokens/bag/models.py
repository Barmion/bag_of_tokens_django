from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Token(models.Model):
    """Описание жетона."""

    name = models.SlugField(
        verbose_name='Название',
        max_length=20
    )
    char = models.CharField(
        verbose_name='Символ/смайл',
        max_length=5
    )
    sticker_id = models.CharField(
        verbose_name='Стикер в телеграмме',
        max_length=50
    )
    image = models.ImageField(
        upload_to='tokens',
        verbose_name='Изображение',
        blank=True
    )
    ordering = models.PositiveSmallIntegerField(
        verbose_name='Порядок выдачи',
        default=0
    )

    class Meta:
        verbose_name = 'жетон'
        verbose_name_plural = 'Жетоны'
        ordering = ('ordering',)

    def __str__(self):
        return self.name


class Bag(models.Model):
    """Описание мешка."""

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bags',
        verbose_name='Владелец'
    )
    token = models.ForeignKey(
        Token,
        on_delete=models.CASCADE,
        related_name='bags',
        verbose_name='Жетон'
    )

    class Meta:
        verbose_name = 'мешок'
        verbose_name_plural = 'Мешки'
        ordering = ('owner', 'token__ordering',)

    def __str__(self):
        return self.owner.username
