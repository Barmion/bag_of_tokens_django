from django.db import models
from django.contrib.auth import get_user_model

from bag.models import Token

User = get_user_model()


class Statistic_1(models.Model):
    """Статистика 1. По токенам."""

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='stat_1',
        verbose_name='Владелец'
    )
    token = models.ForeignKey(
        Token,
        on_delete=models.CASCADE,
        related_name='stat_1',
        verbose_name='Жетон'
    )

    class Meta:
        verbose_name = 'Статистика 1'
        verbose_name_plural = 'Статистика 1'
        ordering = ('owner', 'token__ordering',)

    def __str__(self):
        return self.owner.username


class Statistic_2(models.Model):
    """Статистика 2. Таблица."""
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='stat_2',
        verbose_name='Владелец'
    )
    plus_one_tokens = models.IntegerField(default=0)
    zero_tokens = models.IntegerField(default=0)
    minus_one_tokens = models.IntegerField(default=0)
    minus_two_tokens = models.IntegerField(default=0)
    minus_tree_tokens = models.IntegerField(default=0)
    minus_four_tokens = models.IntegerField(default=0)
    minus_five_tokens = models.IntegerField(default=0)
    minus_six_tokens = models.IntegerField(default=0)
    minus_seven_tokens = models.IntegerField(default=0)
    minus_eight_tokens = models.IntegerField(default=0)
    star_tokens = models.IntegerField(default=0)
    tentacle_tokens = models.IntegerField(default=0)
    kthulhu_tokens = models.IntegerField(default=0)
    hood_tokens = models.IntegerField(default=0)
    skull_tokens = models.IntegerField(default=0)
    tablet_tokens = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Статистика 2'
        verbose_name_plural = 'Статистика 2'

    def __str__(self):
        return self.owner.username
