from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import viewsets

from bag.models import Bag

from .serializers import BagBotSerializer, BagSerializer

# from statistic.views import stat_1_update, stat_2_update


User = get_user_model()


class BagListViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        if self.request.user.is_telegram_bot:
            return Bag.objects.filter(
                owner__telegram_id=self.kwargs.get('owner')
            )
        return Bag.objects.filter(owner=self.request.user)

    def get_serializer_class(self, *args, **kwargs):
        if self.request.user.is_telegram_bot:
            return BagBotSerializer
        return BagSerializer

    def get_object(self):
        if self.action == 'retrieve':
            return self.get_queryset().order_by('?').first()
        return get_list_or_404(
            self.get_queryset(),
            token__char=self.request.data.get('token')
        )[0]

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     # stat_1_update(owner=request.user, token=instance)
    #     # stat_2_update(owner=request.user, token=instance.name)
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)
