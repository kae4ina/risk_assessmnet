from django.shortcuts import render

from django.shortcuts import render, redirect

from assets.models import Asset
from .models import UserThreat, CompanyThreat, AssetThreat
from .forms import UserThreatForm
from django.http import JsonResponse


def threat_create_view(request):
    if request.method == 'POST':
        form = UserThreatForm(request.POST, initial={'user': request.user})
        if form.is_valid():
            threat = form.save()
            related_assets = form.cleaned_data['related_assets']


            for asset in related_assets:
                AssetThreat.objects.create(threat=threat, asset=asset)


            return redirect('threat_saved')

    else:
        form = UserThreatForm(initial={'user': request.user})

    return render(request, 'threat/threat_create.html', {'form': form})




def load_assets(request):
    company_id = request.GET.get('company_id')
    assets = Asset.objects.filter(company_id=company_id).values('id', 'name')
    return JsonResponse(list(assets), safe=False)



def threat_saved(request):
 return render(request, 'threat/threat_saved.html')

