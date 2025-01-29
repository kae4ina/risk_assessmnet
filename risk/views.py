from django.http import JsonResponse
from django.shortcuts import render, redirect

from assets.models import Asset
from risk.forms import RiskForm
from threat.models import UserThreat


def risk_create(request):
    if request.method == 'POST':
        form = RiskForm(request.POST)
        if form.is_valid():
            risk = form.save(commit=False)
            risk.user = request.user
            risk.save()
            return redirect('risk_saved')
    else:
        form = RiskForm()

    context = {
        'form': form,
    }

    return render(request, 'risk/risk_create.html', context)

def load_threat(request):
    user_id = request.user.id
    threats = UserThreat.objects.filter(user_id=user_id).values('id', 'name')
    return JsonResponse(list(threats), safe=False)

def risk_saved(request):
    return render(request, 'risk/risk_saved.html')


# Create your views here.
