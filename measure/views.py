from django.http import JsonResponse
from django.shortcuts import render, redirect

from company.models import CompanyUser
from measure.froms import UserMeasureForm
from risk.models import Risk


# Create your views here.

def measure_create(request):
    if request.method == 'POST':
        form = UserMeasureForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('measure_saved')
    else:
        form = UserMeasureForm(user=request.user)

    return render(request, 'measure/measure_create.html', {
        'form': form,
    })
    return render(request, 'measure/measure_create.html', {'form': form})

def get_risk(request):
    company_id = request.GET.get('company_id')
    risks = Risk.objects.filter(related_company_id=company_id).values('id', 'name')
    risk_list = list(risks)
    return JsonResponse(risk_list, safe=False)

def measure_saved(request):
    return render(request, 'measure/measure_saved.html')
