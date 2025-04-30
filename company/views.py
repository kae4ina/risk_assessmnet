from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect

from assets.models import Asset
from measure.models import UserMeasure
from risk.models import Risk
from threat.models import AssetThreat
from vulnerability.models import UserVulnerabilityAsset
from .forms import CompanyForm
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CompanyUser, Company


@login_required
def company_create(request):
    if request.method == 'POST':
        form_company=CompanyForm(request.POST)
        if form_company.is_valid():
            company=form_company.save()
            company_user=CompanyUser(company=company, user=request.user)
            company_user.save()
            return redirect('company_saved')
    else:
        form_company = CompanyForm()



    return render(request, 'company/company_create.html', {'form': form_company})

def company_saved(request):
    return render(request,'accounts/user_companies.html')



class UserCompaniesView(LoginRequiredMixin, ListView):
    model = CompanyUser
    template_name = 'accounts/user_companies.html'
    context_object_name = 'company_users'

    def get_queryset(self):
        # Получаем все компании, связанные с текущим пользователем
        return CompanyUser .objects.filter(user=self.request.user)


@login_required
def company_assets(request, company_id):
    assets = Asset.objects.filter(company_id=company_id)

    for asset in assets:
        # Получаем уязвимости для актива
        asset.user_vulnerabilities = UserVulnerabilityAsset.objects.filter(asset=asset).select_related('vulnerability')

        # Получаем угрозы для актива через модель AssetThreat
        asset.user_threats = AssetThreat.objects.filter(asset=asset).select_related('threat')

    context = {
        'assets': assets,
    }
    return render(request, 'accounts/company_assets.html', context)
# Create your views here.