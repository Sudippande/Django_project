# this is the step comes after the registration in app. here we create a firm from django


from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model=Tweet
        fields=['text','photo']


#now here we will add user registrations
class UserRegistrationForm(UserCreationForm):
    email= forms.EmailField()
    class meta:
        model=User
        fields=('username''email','password1','password2')