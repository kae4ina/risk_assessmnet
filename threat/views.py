from django.shortcuts import render

from django.shortcuts import render, redirect

from assets.models import Asset
from .models import UserThreat
from .forms import UserThreatForm
from django.http import JsonResponse

def threat_create_view(request):
    if request.method == 'POST':
            form = UserThreatForm(request.POST, user=request.user)
            if form.is_valid():
                user_threat = form.save(commit=False)
                user_threat.user=request.user
                user_threat=form.save()
                return redirect('threat_saved')
    else:
        form = UserThreatForm(user=request.user)

    context = {
        'form': form,
    }

    return render(request, 'threat/threat_create.html', context)

def load_assets(request):
    company_id = request.GET.get('company_id')
    assets = Asset.objects.filter(company_id=company_id).values('id', 'name')
    return JsonResponse(list(assets), safe=False)


def threat_saved(request):
    return render(request, 'threat/threat_saved.html')

