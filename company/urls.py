from django.urls import path
from .views import company_create, company_saved

urlpatterns = [
    path('companycreate/', company_create, name='company_create'),
    path('companysaved/',company_saved, name='company_saved')
]