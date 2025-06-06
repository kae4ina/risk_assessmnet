# urls.py
from django.urls import path
from .views import create_risk, load_threat_ways, risk_created_success, load_all_ways, user_risks, risk_measures, \
    risk_detail, get_risks

urlpatterns = [
    path('create/', create_risk, name='create_risk'),
    path('ajax/load-threat-ways/', load_threat_ways, name='load_threat_ways'),
    path('risk-created-success/', risk_created_success, name='risk_created_success'),
    path('load-all-ways/', load_all_ways, name='load_all_ways'),
    path('my-risks/', user_risks, name='user_risks'),
    path('risk/<int:risk_id>/measures/', risk_measures, name='risk_measures'),
    path('risk/<int:risk_id>/', risk_detail, name='risk_detail'),
    path('get_risks/', get_risks, name='get_risks'),
]