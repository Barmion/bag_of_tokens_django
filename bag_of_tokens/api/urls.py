from django.urls import include, path

from api.views import BagListViewSet

urlpatterns = [
    path('bag/', BagListViewSet.as_view({'get': 'list'})),
    path('random/', BagListViewSet.as_view({'get': 'retrieve'})),
    path('add/', BagListViewSet.as_view({'post': 'create'})),
    path('delete/', BagListViewSet.as_view({'delete': 'destroy'})),
    path('', include('djoser.urls.jwt')),
]
