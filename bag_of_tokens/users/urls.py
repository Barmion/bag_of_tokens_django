from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'users'

urlpatterns = [
    path('',
         views.ProfileListView.as_view(),
         name='profile'),
    path('edit_profile',
         views.ProfileUpdateView.as_view(),
         name='edit_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)