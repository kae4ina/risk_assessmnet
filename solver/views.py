from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from .models import ThreatWays, GeneralThreats, Ways, UserRisk
from .forms import RiskCreationForm


@login_required
def create_risk(request):
    if request.method == 'POST':
        form = RiskCreationForm(request.POST)
        if form.is_valid():
            risk = form.save(commit=False)
            risk.user = request.user
            risk.save()

            risk.threats.set(form.cleaned_data['threats'])
            risk.ways.set(form.cleaned_data['ways'])

            return redirect('risk_created_success')
    else:
        form = RiskCreationForm()

    return render(request, 'solver/create_risk.html', {'form': form})


@require_GET
def load_threat_ways(request):
    threat_ids = request.GET.getlist('threat_ids[]', [])


    threat_ways = ThreatWays.objects.filter(
        generalthreat_id__in=threat_ids
    ).select_related('way', 'generalthreat', 'way__group')

    data = []
    for tw in threat_ways:
        data.append({
            'id': tw.id,
            'threat_id': tw.generalthreat.id,
           'threat_name': tw.generalthreat.name,
            'way_name': tw.way.name,


        })

    return JsonResponse({'ways': data})

@login_required
def risk_created_success(request):
    return render(request, 'solver/user_risks.html')

@require_GET
def load_all_ways(request):
    ways = Ways.objects.all().select_related('group')
    data = [{
        'id': way.id,
        'name': way.name,
        'group_id': way.group.id,
        'group_name': way.group.name
    } for way in ways]
    return JsonResponse({'ways': data})


@login_required
def user_risks(request):
    risks = UserRisk.objects.filter(user=request.user) \
        .select_related('general_object', 'user') \
        .prefetch_related('threats', 'ways') \
        .order_by('-created_at')

    return render(request, 'solver/user_risks.html', {'risks': risks})