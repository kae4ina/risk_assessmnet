from django.http import JsonResponse
from django.shortcuts import render, redirect

from assets.models import Asset
from risk.forms import RiskForm
from threat.models import UserThreat, CompanyThreat


def risk_create(request):
    if request.method == 'POST':
        form = RiskForm(request.POST, user=request.user)
        if form.is_valid():
            risk = form.save(commit=False)
            risk.save()
            return redirect('risk_saved')
    else:
        form = RiskForm(user=request.user)

    context = {
        'form': form,
    }

    return render(request, 'risk/risk_create.html', context)

def load_threat(request):
    asset_id = request.GET.get('asset_id')
    company_id = request.GET.get('company_id')  # Получаем ID компании
    threats = CompanyThreat.objects.filter(company_id=company_id, threat__related_asset_id=asset_id).select_related(
        'threat')

    data = [{'id': ct.threat.id, 'name': ct.threat.name} for ct in threats]
    return JsonResponse(data, safe=False)

def risk_saved(request):
    return render(request, 'risk/risk_saved.html')


# Create your views here.
