from django.urls import path

from assets.views import CompanyAssetsView
from .views import company_create, company_saved, UserCompaniesView, company_assets

urlpatterns = [
    path('companycreate/', company_create, name='company_create'),
    path('companysaved/',company_saved, name='company_saved'),
    path('my-companies/', UserCompaniesView.as_view(), name='my_companies'),
    path('assets/my-companies/<int:company_id>/assets/', company_assets, name='company_assets'),


]