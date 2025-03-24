from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from assets.models import Asset
from risk.forms import RiskForm
from risk.models import Risk, RiskVulnerability, RiskThreat
from threat.models import UserThreat, CompanyThreat
from vulnerability.models import UserVulnerability
from django.views.generic import ListView


def risk_create(request):
    if request.method == 'POST':
        form = RiskForm(request.POST, user=request.user)
        if form.is_valid():
            # Сохраняем риск
            risk = form.save(commit=False)
            risk.save()  # Сначала сохраняем сам риск

            # Сохраняем связанные угрозы
            related_threats = form.cleaned_data.get('related_threats')
            for threat in related_threats:
                RiskThreat.objects.create(risk=risk, threat=threat)

            # Сохраняем связанные уязвимости
            related_vulnerabilities = form.cleaned_data.get('related_vulnerabilities')
            for vulnerability in related_vulnerabilities:
                RiskVulnerability.objects.create(risk=risk, vulnerability=vulnerability)

            return redirect('risk_saved')
    else:
        form = RiskForm(user=request.user)
    return render(request, 'risk/risk_create.html', {'form': form})



def get_threats_and_vulnerabilities(request):
    asset_ids = request.GET.getlist('asset_ids')  # Получаем список asset_ids

    # Получаем угрозы через промежуточную модель AssetThreat
    threats = UserThreat.objects.filter(assetthreat__asset_id__in=asset_ids).values('id', 'name').distinct()

    # Получаем уязвимости через промежуточную модель UserVulnerabilityAsset
    vulnerabilities = UserVulnerability.objects.filter(uservulnerabilityasset__asset_id__in=asset_ids).values('id', 'name').distinct()

    return JsonResponse({
        'threats': list(threats),
        'vulnerabilities': list(vulnerabilities)
    })


def risk_saved(request):
    return render(request, 'risk/risk_saved.html')

def get_assets(request):
    company_id = request.GET.get('company_id')
    assets = Asset.objects.filter(company_id=company_id).values('id', 'name')
    return JsonResponse({'assets': list(assets)})

def get_threats_and_vulnerabilities(request):
    asset_id = request.GET.get('asset_id')
    threats = UserThreat.objects.filter(related_asset_id=asset_id).values('id', 'name')
    vulnerabilities = UserVulnerability.objects.filter(related_asset_id=asset_id).values('id', 'name')
    return JsonResponse({'threats': list(threats), 'vulnerabilities': list(vulnerabilities)})

class CompanyRiskView(LoginRequiredMixin, ListView):
    model = Risk
    template_name = 'accounts/company_risk.html'
    context_object_name = 'risks'

    def get_queryset(self):
        # Получаем ID компании из URL и извлекаем ее активы
        company_id = self.kwargs['company_id']
        return Risk.objects.filter(related_company_id=company_id)

def risk_detail_view(request, risk_id):
    risk = get_object_or_404(Risk, id=risk_id)
    return render(request, 'company_risk.html', {'risk': risk})
# Create your views here.
