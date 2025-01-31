from django.http import JsonResponse
from django.shortcuts import render, redirect

from assets.models import Asset
from risk.forms import RiskForm
from threat.models import UserThreat, CompanyThreat
from vulnerability.models import UserVulnerability


def risk_create(request):
    if request.method == 'POST':
        form = RiskForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('risk_saved')
    else:
        form = RiskForm(user=request.user)
    return render(request, 'risk/risk_create.html', {'form': form})


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


# Create your views here.
