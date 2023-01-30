from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Comments


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя:', help_text='', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': "off"}))
    password = forms.CharField(label='Пароль:', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя:', help_text='', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': "off"}))
    password1 = forms.CharField(label='Пароль:', help_text='Пароль должен состоять из букв и цифр', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля:', help_text='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail:', widget=forms.EmailInput(attrs={'class': 'form-control', 'autocomplete': "off"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CommentForm(forms.ModelForm):
    text_com = forms.CharField(label='Текст комментария:', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': "off"}))

    class Meta:
        model = Comments
        fields = ('text_com',)

