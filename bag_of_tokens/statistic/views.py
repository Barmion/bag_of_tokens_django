from django.forms.models import model_to_dict
from django.contrib.auth import get_user_model

from .models import Statistic_1, Statistic_2

User = get_user_model()


def stat_1_update(owner, token):
    Statistic_1.objects.create(owner=owner, token=token)


def stat_2_update(owner, token):
    object, created = Statistic_2.objects.get_or_create(owner=owner)
    setattr(object, token, getattr(object, token) + 1)
    object.save()


def get_stat_2(owner):
    return model_to_dict(Statistic_1.objects.get_or_create(owner=owner))
