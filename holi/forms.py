from cProfile import label
from attr import field
from django import forms
from .models import Image
class ImageForm(forms.ModelForm):
    class Meta:
        model =Image
        fields = ('__all__')
        labels={'photo':''}