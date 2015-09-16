from django.forms import ModelForm, TextInput, EmailInput
from .models import Gamers

class GamersForm(ModelForm):
    pass
    class Meta:
        model = Gamers
        exclude = []
        widgets = {'FirstName': TextInput(attrs={'class': 'form-control'}),
                   'LastName': TextInput(attrs={'class': 'form-control'}),
                   'Email': EmailInput(attrs={'class': 'form-control'})}


