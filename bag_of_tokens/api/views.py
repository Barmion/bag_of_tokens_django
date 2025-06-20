from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from bag.models import Bag
from statistic.views import stat_2_update
from statistic.models import Statistic_2

from .serializers import BagBotSerializer, BagSerializer, StatisticSerializer

User = get_user_model()


class BagListViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        if self.request.user.is_telegram_bot:
            return Bag.objects.filter(
                owner__telegram_id=self.request.data.get('owner')
            )
        return Bag.objects.filter(owner=self.request.user)

    def get_serializer_class(self, *args, **kwargs):
        if self.request.user.is_telegram_bot:
            return BagBotSerializer
        return BagSerializer

    def get_object(self):
        if self.action == 'retrieve':
            return get_list_or_404(
                self.get_queryset().order_by('?'),
            )[0]
        return get_list_or_404(
            self.get_queryset(),
            token__char=self.request.data.get('token')
        )[0]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.user.is_telegram_bot:
            owner = User.objects.get(
                telegram_id=self.request.data.get('owner'),
            )
        else:
            owner = request.user
        stat_2_update(owner=owner, token=instance.token.name)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class StatisticViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StatisticSerializer

    def get_object(self):
        return Statistic_2.objects.get_or_create(owner=self.request.user)[0]
