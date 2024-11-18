from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import gettext_lazy as _

from .models import User, Review, Customer, ShippingAddress


class LoginForm(AuthenticationForm):
    """Аутентификация пользователя"""
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': _('Имя пользователя')}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': _('Пароль')}))


class RegistrationForm(UserCreationForm):
    """Регистрация пользователя"""
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': _('Пароль')}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': _('Подтвердите пароль')}))

    class Meta:
        model = User
        fields = ('username', 'email',)
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Имя пользователя')}),
                   'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('Почта')})}


class ReviewForm(forms.ModelForm):
    """Форма для отзыва"""

    class Meta:
        model = Review
        fields = ('text', 'grade')
        widgets = {'text': forms.Textarea(attrs={'class': 'form-control',
                                                 'placeholder': _('Ваш отзыв')}),
                   'grade': forms.Select(attrs={'class': 'form-control',
                                                'placeholder': _('Ваша оценка')})}


class CustomerForm(forms.ModelForm):
    """Контактная информация"""

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'phone')
        widgets = {'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Имя')}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Фамилия')}),
                   'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('Email')}),
                   'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Телефон')}),
                   }


class ShippingForm(forms.ModelForm):
    """Адрес доставки"""

    class Meta:
        model = ShippingAddress
        fields = ('city', 'state', 'street')
        widgets = {'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Город')}),
                   'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Район')}),
                   'street': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Улица/дом/квартира')}),
                   }
