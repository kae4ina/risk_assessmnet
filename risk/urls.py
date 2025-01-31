from django.urls import path

from risk.views import risk_create, load_threats, risk_saved

urlpatterns = [
    path('risk_create/', risk_create, name='risk_create'),
    path('load_threats/', load_threats, name='load_threats'),
    path('risk_saved/', risk_saved, name='risk_saved'),
]
