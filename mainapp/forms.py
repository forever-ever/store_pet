from django import forms
from . import models


class BlanketProductForm(forms.ModelForm):
    class Meta():
        model = models.BlanketProduct
        fields = '__all__'
        labels = {
            'weight': 'Ширина',
            'height': 'Высота',
        }
