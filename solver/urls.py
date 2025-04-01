# urls.py
from django.urls import path
from .views import create_risk, load_threat_ways

urlpatterns = [
    path('create/', create_risk, name='create_risk'),
    path('ajax/load-threat-ways/', load_threat_ways, name='load_threat_ways'),
]