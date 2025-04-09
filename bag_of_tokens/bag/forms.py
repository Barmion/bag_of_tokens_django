from django import forms

from .models import Bag


class BagForm(forms.ModelForm):

    class Meta:
        model = Bag
        fields = ('token',)
