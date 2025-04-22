from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from users.forms import UserRegistrationForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/registration/',
         CreateView.as_view(
             template_name='registration/registration_form.html',
             form_class=UserRegistrationForm,
             success_url=reverse_lazy('about'),
         ),
         name='registration'),
    path('profile/', include('users.urls')),
    path('bag/', include('bag.urls')),
    path('api/v1/', include('api.urls')),
    path('', TemplateView.as_view(template_name='pages/about.html'),
         name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
