from django import forms
from .models import contactuser

class contactform(forms.ModelForm):
      class Meta:
            model = contactuser()
            fields = '__all__'
