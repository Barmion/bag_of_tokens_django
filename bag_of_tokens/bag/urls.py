from django.urls import path

from .views import AddToken, DeleteToken, RandomToken

app_name = 'bag'

urlpatterns = [
    path('add/', AddToken.as_view(), name='add'),
    path('delete/<int:pk>', DeleteToken.as_view(), name='delete'),
    path('random/', RandomToken.as_view(), name='random')
]
