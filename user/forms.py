from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, FileInput

from user.models import UserProfile


class SignUpForm(UserCreationForm):
    username    = forms.CharField(max_length = 30, label = 'Kullanıcı Adı')
    first_name  = forms.CharField(max_length = 100, label = 'Adınız ')
    last_name  = forms.CharField(max_length = 100, label = 'Soyadınız ')
    email       = forms.EmailField(max_length = 200, label = 'Email ')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', )


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ( 'username','email','first_name','last_name')
        widgets = {
            'username'  : TextInput(attrs={'class': 'input'}),
            'email'     : EmailInput(attrs={'class': 'input'}),
            'first_name': TextInput(attrs={'class': 'input'}),
            'last_name' : TextInput(attrs={'class': 'input' }),
        }

CITY = [
    ('Istanbul', 'Istanbul'),
    ('Ankara', 'Ankara'),
    ('Izmir', 'Izmir'),
    ('Sivas', 'Sivas'),
]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city','country')
        widgets = {
            'phone'     : TextInput(attrs={'class': 'input'}),
            'address'   : TextInput(attrs={'class': 'input'}),
            'city'      : Select(attrs={'class': 'input'},choices=CITY),
            'country'   : TextInput(attrs={'class': 'input' }),
        }