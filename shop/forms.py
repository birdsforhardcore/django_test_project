from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User, Review


class LoginForm(AuthenticationForm):
    """Аутентификация пользователя"""
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Пароль'}))


class RegistrationForm(UserCreationForm):
    """Регистрация пользователя"""
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'email',)
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Почта'})}


class ReviewForm(forms.ModelForm):
    """Форма для отзыва"""

    class Meta:
        model = Review
        fields = ('text', 'grade')
        widgets = {'text': forms.Textarea(attrs={'class': 'form-control',
                                                 'placeholder': 'Ваш отзыв'}),
                   'grade': forms.Select(attrs={'class': 'form-control',
                                                'placeholder': 'Ваша оценка'})}

