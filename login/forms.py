from django import forms
from .models import DatosUser
from django.contrib.auth.forms import UserCreationForm


class CustomUser(UserCreationForm):
    pass


class FormDatosUser(forms.ModelForm):
    class Meta:
        model = DatosUser
        fields = '__all__'
