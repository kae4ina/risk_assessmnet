# assets/urls.py
from django.template.defaulttags import url
from django.urls import path
from . import views
from .views import asset_saved

urlpatterns = [
    path('choose/', views.assets_choose, name='assets_choose'),
    path('assetsaved/', asset_saved, name='asset_saved'),


]