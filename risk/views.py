from django.http import JsonResponse
from django.shortcuts import render, redirect

from assets.models import Asset
from risk.forms import RiskForm
from threat.models import UserThreat, CompanyThreat


def risk_create(request):
    if request.method == 'POST':
        form = RiskForm(request.POST)
        if form.is_valid():
            form.save()
            # Перенаправление или отображение сообщения об успехе
    else:
        form = RiskForm()
    return render(request, 'risk/risk_create.html', {'form': form})

def risk_saved(request):
    return render(request, 'risk/risk_saved.html')


# Create your views here.
