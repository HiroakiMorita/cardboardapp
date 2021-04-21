from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    last_name = forms.CharField(max_length=10, label='苗字')
    first_name = forms.CharField(max_length=10, label='名前')
    email = forms.EmailField(max_length=50,label='Eメールアドレス')
    
    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'email')


class UserForm(forms.ModelForm):
    # 自分で指定する
    username = forms.CharField(max_length=10, label='ユーザー名')
    last_name = forms.CharField(max_length=10, label='苗字')
    first_name = forms.CharField(max_length=10, label='名前')
    email = forms.EmailField(max_length=50,label='Eメールアドレス')
    
    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'email')


class PhotoForm(forms.Form):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'customfile-input'}))
    