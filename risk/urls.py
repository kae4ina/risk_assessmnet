from django.urls import path

from risk.views import risk_create, risk_saved, get_threats_and_vulnerabilities, get_assets

urlpatterns = [
    path('risk_create/', risk_create, name='risk_create'),
    #path('load_threats/', load_threats, name='load_threats'),
    path('risk_saved/', risk_saved, name='risk_saved'),
    path('get_assets/', get_assets, name='get_assets'),
    path('get_threats-_and_vulnerabilities/', get_threats_and_vulnerabilities, name='get_threats_and_vulnerabilities'),
]
