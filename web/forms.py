from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):  #"UserCreationForm" bu ettelatı control elir :password, email, tedade ragamler, sade passwordu ya yox veya username.. duzdu ya yox .
    class Meta:
        model= User
        fields= ['username','email','password1','password2']
