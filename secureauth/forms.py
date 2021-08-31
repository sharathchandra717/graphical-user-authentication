# django.core.files.storage import FileSystemStorage
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

#fs = FileSystemStorage(location='secureauth/static/static_files')

class SignUpForm(UserCreationForm):
    myfile = forms.FileField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'myfile')
