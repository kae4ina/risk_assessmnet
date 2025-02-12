from django.urls import path

from assets.views import CompanyAssetsView
from .views import company_create, company_saved, UserCompaniesView

urlpatterns = [
    path('companycreate/', company_create, name='company_create'),
    path('companysaved/',company_saved, name='company_saved'),
    path('my-companies/', UserCompaniesView.as_view(), name='my_companies'),



]