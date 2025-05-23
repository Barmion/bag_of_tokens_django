from django.urls import include, path

from api.views import BagListViewSet, StatisticViewSet

app_name = 'api_v1'

urlpatterns = [
    path(
        'bag/',
        BagListViewSet.as_view({'get': 'list'}),
        name='bag'
    ),
    path(
        'random/',
        BagListViewSet.as_view({'get': 'retrieve'}),
        name='random'
    ),
    path(
        'add/',
        BagListViewSet.as_view({'post': 'create'}),
        name='add'
    ),
    path(
        'delete/',
        BagListViewSet.as_view({'delete': 'destroy'}),
        name='delete'
    ),
    path(
        'statistic/',
        StatisticViewSet.as_view({'get': 'retrieve'}),
        name='statistic'
    ),
    path('', include('djoser.urls.jwt')),
    path('', include('djoser.urls')),
]
