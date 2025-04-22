from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from bag.models import Bag

User = get_user_model()


class ProfileListView(LoginRequiredMixin, DetailView):
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'telegram_id',)
    template_name = 'user/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tokens'] = Bag.objects.filter(owner=self.request.user).select_related('token')
        return context

    def get_object(self):
        return self.request.user


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'telegram_id',)
    template_name = 'user/update_profile.html'

    def get_object(self):
        return get_object_or_404(
            User,
            username=self.request.user.username,
        )

    def get_success_url(self):
        return reverse('users:profile')
