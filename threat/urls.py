from django.urls import path
from .views import threat_create_view, load_assets, threat_saved

urlpatterns = [
    path('threat_create/', threat_create_view, name='threat_create'),
    path('load_assets/', load_assets, name='load_assets'),
    path('threat_saved/', threat_saved, name='threat_saved'),
]
