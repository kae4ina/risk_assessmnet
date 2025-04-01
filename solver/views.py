from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from .models import ThreatWays, GeneralThreats
from .forms import RiskCreationForm


@login_required
def create_risk(request):
    if request.method == 'POST':
        form = RiskCreationForm(request.POST)
        if form.is_valid():
            risk = form.save(commit=False)
            risk.user = request.user
            risk.save()

            threats = form.cleaned_data.get('threats')
            risk.threats.set(threats)

            threat_ways_ids = request.POST.getlist('threat_ways')
            threat_ways = ThreatWays.objects.filter(id__in=threat_ways_ids)
            risk.threat_ways.set(threat_ways)

            return redirect('risk_created_success')
    else:
        form = RiskCreationForm()

    return render(request, 'solver/create_risk.html', {'form': form})


@require_GET
def load_threat_ways(request):
    threat_ids = request.GET.getlist('threat_ids[]', [])

    # Используем точные имена полей из вашей модели
    threat_ways = ThreatWays.objects.filter(
        generalthreat_id__in=threat_ids  # Используем generalthreat_id вместо generalthreat
    ).select_related('way', 'generalthreat', 'way__group')

    data = []
    for tw in threat_ways:
        data.append({
            'id': tw.id,
            'threat_id': tw.generalthreat.id,  # Используем generalthreat
           'threat_name': tw.generalthreat.name,
            'way_name': tw.way.name,


        })

    return JsonResponse({'ways': data})