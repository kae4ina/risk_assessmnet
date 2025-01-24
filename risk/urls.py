from django.urls import path

from risk.views import load_threats, risk_create

urlpatterns = [
    path('risk_create/', risk_create, name='risk_create'),
    path('load_threats/', load_threats, name='load_threats'),
]