from django.views.generic import CreateView, DeleteView, DetailView
from django.views.generic.edit import ModelFormMixin
from django.urls import reverse_lazy

from .models import Bag
from .forms import BagForm


class AddToken(CreateView):
    form_class = BagForm
    success_url = reverse_lazy('users:profile')
    template_name = 'bag/bag_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    

class DeleteToken(DeleteView):
    model = Bag
    template_name = 'bag/bag_form.html'
    success_url = reverse_lazy('users:profile')


class RandomToken(DetailView):
    model = Bag
    template_name = 'bag/random_token.html'

    def get_object(self):
        return Bag.objects.filter(owner=self.request.user).order_by('?').first()


    
# class ProfileListView(
#     FilterMixin,
#     PostMixin,
#     PaginateMixin,
#     ListView
# ):
#     template_name = 'user/profile.html'

#     def get_queryset(self):
#         if self.kwargs['username'] == self.request.user.username:
#             queryset = super().get_queryset().filter(
#                 author__username=self.kwargs['username']
#             ).annotate(
#                 comment_count=Count('comments')
#             ).order_by('-pub_date')
#         else:
#             queryset = self.get_filtered_queryset()
#         return queryset

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['profile'] = get_object_or_404(
#             User,
#             username=self.kwargs['username'],
#         )
#         return context
