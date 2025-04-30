from django.urls import path

from assets.views import CompanyAssetsView
from risk.views import risk_create, risk_saved, get_threats_and_vulnerabilities, get_assets, CompanyRiskView, \
    risk_detail_view

urlpatterns = [
    path('risk_create/', risk_create, name='risk_create'),
    #path('load_threats/', load_threats, name='load_threats'),
    path('risk_saved/', risk_saved, name='risk_saved'),
    path('get_assets/', get_assets, name='get_assets'),
    path('get_threats-_and_vulnerabilities/', get_threats_and_vulnerabilities, name='get_threats_and_vulnerabilities'),
    path('risk/<int:company_id>/risk/', CompanyRiskView.as_view(), name='company_risk'),
    path('risk/<int:risk_id>/', risk_detail_view, name='risk_detail'),

]
