from django import forms
from .models import Image,Profile,Comment

class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        exclude=['likes','user','posted_at','comments']
 