from django.urls import path

from risk.views import risk_create_view, load_threat, risk_saved

urlpatterns = [
    path('risk/create/', risk_create_view, name='threat_create'),
    path('load_threat/', load_threat, name='load_assets'),
    path('risk/saved/', risk_saved, name='threat_saved'),
]
