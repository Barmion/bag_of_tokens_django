from django.contrib.auth import get_user_model
from rest_framework import serializers

from bag.models import Bag, Token

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
