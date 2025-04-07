# urls.py
from django.urls import path
from .views import create_risk, load_threat_ways, risk_created_success,  load_all_ways

urlpatterns = [
    path('create/', create_risk, name='create_risk'),
    path('ajax/load-threat-ways/', load_threat_ways, name='load_threat_ways'),
    path('risk-created-success/', risk_created_success, name='risk_created_success'),
    path('load-all-ways/', load_all_ways, name='load_all_ways'),
]