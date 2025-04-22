from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView

from statistic.views import stat_1_update, stat_2_update

from .forms import BagForm
from .mixins import OnlyAuthorMixin
from .models import Bag


class AddToken(LoginRequiredMixin, CreateView):
    form_class = BagForm
    success_url = reverse_lazy('users:profile')
    template_name = 'bag/bag_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class DeleteToken(OnlyAuthorMixin, LoginRequiredMixin, DeleteView):
    model = Bag
    template_name = 'bag/bag_form.html'
    success_url = reverse_lazy('users:profile')


class RandomToken(LoginRequiredMixin, DetailView):
    model = Bag
    template_name = 'bag/random_token.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        stat_1_update(owner=request.user, token=self.object.token)
        stat_2_update(owner=request.user, token=self.object.token.name)
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_object(self):
        return Bag.objects.filter(
            owner=self.request.user).order_by('?').first()
