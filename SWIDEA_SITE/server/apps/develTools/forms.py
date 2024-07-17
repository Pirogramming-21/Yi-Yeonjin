from django import forms
from .models import DevelTool

class DevelToolForm(forms.ModelForm):
  class Meta():
    model = DevelTool
    fields = ('__all__')