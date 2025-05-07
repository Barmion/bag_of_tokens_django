from django.contrib.auth import get_user_model
from rest_framework import serializers

from bag.models import Bag, Token
from statistic.models import Statistic_2

User = get_user_model()


class BagSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    token = serializers.SlugRelatedField(
        'char',
        read_only=False,
        queryset=Token.objects.all(),
    )

    class Meta:
        model = Bag
        fields = ('token', 'owner')


class BagBotSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        'telegram_id',
        read_only=False,
        queryset=User.objects.all())
    token = serializers.SlugRelatedField(
        'char',
        read_only=False,
        queryset=Token.objects.all(),
    )

    class Meta:
        model = Bag
        fields = ('owner', 'token',)


class StatisticSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Statistic_2
        fields = (
            'owner',
            'star_tokens',
            'plus_one_tokens',
            'zero_tokens',
            'minus_one_tokens',
            'minus_two_tokens',
            'minus_tree_tokens',
            'minus_four_tokens',
            'minus_five_tokens',
            'minus_six_tokens',
            'minus_seven_tokens',
            'minus_eight_tokens',
            'tentacle_tokens',
            'kthulhu_tokens',
            'hood_tokens',
            'skull_tokens',
            'tablet_tokens',
        )
