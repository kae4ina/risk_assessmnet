from django.http import JsonResponse
from django.shortcuts import render, redirect

from assets.models import Asset
from risk.forms import RiskForm
from threat.models import UserThreat, CompanyThreat


def risk_create(request):
    if request.method == 'POST':
        form = RiskForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('risk_saved')
    else:
        form = RiskForm(user=request.user)
    return render(request, 'risk/risk_create.html', {'form': form})

def load_threats(request):
    company_id = request.GET.get('company_id')
    threats = UserThreat.objects.filter(companythreat__company_id=company_id).values('id', 'name')
    return JsonResponse({'threats': list(threats)})

def risk_saved(request):
    return render(request, 'risk/risk_saved.html')


# Create your views here.
