from django.shortcuts import render

from django.shortcuts import render, redirect

from assets.models import Asset
from .models import UserThreat, CompanyThreat
from .forms import UserThreatForm
from django.http import JsonResponse

def threat_create_view(request):
    if request.method == 'POST':
        form = UserThreatForm(request.POST, user=request.user)
        if form.is_valid():
            # Сохраняем объект UserThreat, но не коммитим в базу данных
            user_threat = form.save(commit=False)
            user_threat.user = request.user  # Если у вас есть поле user в UserThreat
            user_threat.save()  # Сохраняем объект UserThreat в базу данных

            # Получаем ID компании из формы
            company_id = form.cleaned_data['company'].id

            # Создаем запись в таблице CompanyThreat
            company_threat = CompanyThreat(company_id=company_id, threat=user_threat)
            company_threat.save()  # Сохраняем объект CompanyThreat в базу данных

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

