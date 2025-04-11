from django.db.models import Count, Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from .models import ThreatWays, GeneralThreats, Ways, UserRisk, DefaultMeasure, DefaultMeasureGroup
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


            ways_ids = form.cleaned_data['ways'].split(',')
            ways_ids = [id.strip() for id in ways_ids if id.strip()]
            risk.ways.set(ways_ids)

            return redirect('user_risks')
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
    return render(request, 'solver/risk_created_success.html')


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
        .select_related('general_object') \
        .prefetch_related('threats', 'ways') \
        .order_by('-created_at')

    return render(request, 'solver/user_risks.html', {'risks': risks})


@login_required
def risk_detail(request, risk_id):
    risk = get_object_or_404(
        UserRisk.objects.select_related('general_object')
        .prefetch_related('threats', 'ways'),
        pk=risk_id,
        user=request.user
    )
    return render(request, 'solver/risk_detail.html', {'risk': risk})


@login_required
def risk_measures(request, risk_id):
    risk = get_object_or_404(UserRisk.objects.prefetch_related('threats'), pk=risk_id, user=request.user)
    threat_ids = risk.threats.values_list('id', flat=True)

    # базовый queryset мер
    measures = DefaultMeasure.objects.filter(
        rulesthreat__threat_id__in=threat_ids
    ).select_related('subgroup__group').distinct()

    #  топ-10 мер
    top_measures = measures.order_by('-koef')[:10]


    view_type = request.GET.get('view', 'all')
    sort = request.GET.get('sort')
    group_filter = request.GET.get('group')

    # фильтры только для режима "все меры"
    if view_type == 'all':
        if group_filter:
            measures = measures.filter(subgroup__group_id=group_filter)

        if sort == 'asc':
            measures = measures.order_by('koef')
        elif sort == 'desc':
            measures = measures.order_by('-koef')

    measure_groups = DefaultMeasureGroup.objects.filter(
        defaultmeasuresubgroup__defaultmeasure__in=measures
    ).distinct()

    return render(request, 'solver/risk_measures.html', {
        'risk': risk,
        'measures': measures,
        'top_measures': top_measures,
        'measure_groups': measure_groups,
        'selected_group': group_filter,
        'current_sort': sort,
        'current_view': view_type,
    })