# this is the step comes after the registration in app. here we create a firm from django


from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model=Tweet
        fields=['text','photo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Apply Bootstrap styling to all fields
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

        # Optional: Customize specific fields
        if 'image' in self.fields:
            self.fields['image'].widget.attrs.update({'class': 'form-control-file'})


#now here we will add user registrations
class UserRegistrationForm(UserCreationForm):
    email= forms.EmailField()
    class Meta:
        model=User
        fields=('username','email','password1','password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = '' 
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label
            })