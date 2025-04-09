from django.contrib.auth import get_user_model
from rest_framework import viewsets

from bag.models import Bag

from .serializers import BagBotSerializer, BagSerializer

User = get_user_model()


class BagListViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        if self.request.user.is_telegram_bot:
            return Bag.objects.filter(
                owner__telegram_id=self.request.kwargs.get('telegram_id')
            )
        return Bag.objects.filter(owner=self.request.user)

    def get_serializer_class(self, *args, **kwargs):
        if self.request.user.is_telegram_bot:
            return BagBotSerializer
        return BagSerializer

    def get_object(self):
        if self.action == 'retrieve':
            return self.get_queryset().order_by('?').first()  # Get random token
        return self.get_queryset().filter(
            token__char=self.request.data.get('token')
        ).first()
