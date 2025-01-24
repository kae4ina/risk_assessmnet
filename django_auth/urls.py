"""
URL configuration for django_auth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path('mainmenu',TemplateView.as_view(template_name="main_menu.html"),name="mainmenu"),# new
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="zero_page.html"), name="start"),
    path("home", TemplateView.as_view(template_name="home.html"), name="home"),
    path('assets/', include('assets.urls')),  # Подключаем URL-адреса приложения assets
    #path('login/', views.login_view, name='login'),
    path('company/', include('company.urls')),
    path('vulnerability/', include('vulnerability.urls')),
    path('threat/',include('threat.urls')),
   # path('risk/',include('risk.urls')),


]
