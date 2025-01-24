from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from assets.models import Asset
from company.models import CompanyUser
from threat.models import UserThreat
from .forms import RiskForm

def risk_create(request):
    if request.method == 'POST':
        form = RiskForm(request.POST, user=request.user)
        if form.is_valid():
            risk = form.save(commit=False)
            risk.save()
            return redirect('risk/risk_saved')
    else:
        form = RiskForm(user=request.user)
    return render(request, 'risk/risk_create.html', {'form': form})


def load_threats(request):

        company_user_id = request.GET.get('company_id')
        company_id=CompanyUser.objects.get(id=company_user_id).company_id

        # получаем активы, связанные с данной компанией
        assets = Asset.objects.filter(company_id=company_id)

        # получаем угрозы, связанные с этими активами
        threats = UserThreat.objects.filter(related_asset__in=assets)


        threat_list = [{'id': threat.id, 'name': threat.name} for threat in threats]


        return JsonResponse({'options': threat_list})
