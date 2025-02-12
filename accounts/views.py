from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class CustomLoginView(LoginView):
    def get_success_url(self):
        return reverse_lazy('my_companies')