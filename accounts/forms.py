#import self
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Убираем сообщения о требованиях
            self.fields['username'].help_text = None
            self.fields['email'].help_text = None
            self.fields['password1'].help_text = None
            self.fields['password2'].help_text = None
            self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
            self.fields['email'].widget.attrs['placeholder'] = 'Введите ваш email'
            self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
            self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'
