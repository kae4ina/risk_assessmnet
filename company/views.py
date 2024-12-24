from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import CompanyForm


def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save('company_saved')  # Сохранение данных в БД
            return redirect('company_saved')  # Замените 'success_url' на нужный вам URL
    else:
        form = CompanyForm()

    return render(request, 'company/company_create.html', {'form': form})

def company_saved(request):
    return render(request,'company/company_saved.html')
# Create your views here.
