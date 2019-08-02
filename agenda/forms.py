from django.forms import ModelForm
from .models import *

class ContatoForm(ModelForm):
    class Meta:
        model = Contatos
        fields = ('name', 'number')