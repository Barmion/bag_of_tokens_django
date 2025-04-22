from django.forms.models import model_to_dict
from django.contrib.auth import get_user_model
from django.db.models import Count, Q

from .models import Statistic_1, Statistic_2

User = get_user_model()


def stat_1_update(owner, token):
    Statistic_1.objects.create(owner=owner, token=token)


# def get_stat_1(owner):
#     owner_user = User.objects.get_or_create(username=owner.username)
#     owner_user.annotate(
#         plus_one_tokens=Count('stat_1__token', filter=Q(token.name='plus_one_tokens'))
#     zero_tokens = models.IntegerField(default=0)
#     minus_one_tokens = models.IntegerField(default=0)
#     minus_two_tokens = models.IntegerField(default=0)
#     minus_tree_tokens = models.IntegerField(default=0)
#     minus_four_tokens = models.IntegerField(default=0)
#     minus_five_tokens = models.IntegerField(default=0)
#     minus_six_tokens = models.IntegerField(default=0)
#     minus_seven_tokens = models.IntegerField(default=0)
#     minus_eight_tokens = models.IntegerField(default=0)
#     star_tokens = models.IntegerField(default=0)
#     tentacle_tokens = models.IntegerField(default=0)
#     kthulhu_tokens = models.IntegerField(default=0)
#     hood_tokens = models.IntegerField(default=0)
#     skull_tokens = models.IntegerField(default=0)
#     tablet_tokens = models.IntegerField(default=0))
#     return 


def stat_2_update(owner, token):
    object, created = Statistic_2.objects.get_or_create(owner=owner)
    setattr(object, token, getattr(object, token) + 1)
    object.save()


def get_stat_2(owner):
    return model_to_dict(Statistic_1.objects.get_or_create(owner=owner))
