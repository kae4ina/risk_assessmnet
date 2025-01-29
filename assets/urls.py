# assets/urls.py
from django.template.defaulttags import url
from django.urls import path
from . import views
from .views import asset_saved, CompanyAssetsView

urlpatterns = [
    path('choose/', views.assets_choose, name='assets_choose'),
    path('asset_saved/', asset_saved, name='asset_saved'),
    path('my-companies/<int:company_id>/assets/', CompanyAssetsView.as_view(), name='company_assets'),


]