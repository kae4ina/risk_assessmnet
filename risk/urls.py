from django.urls import path

from risk.views import risk_create, load_threat, risk_saved

urlpatterns = [
    path('risk_create/', risk_create, name='risk_create'),
    path('load_threat/', load_threat, name='load_threat'),
    path('risk_saved/', risk_saved, name='risk_saved'),
]
