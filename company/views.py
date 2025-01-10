from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import CompanyForm
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CompanyUser

@login_required
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



class UserCompaniesView(LoginRequiredMixin, ListView):
    model = CompanyUser
    template_name = 'accounts/user_companies.html'  # Укажите путь к вашему шаблону
    context_object_name = 'company_users'  # Имя переменной в контексте

    def get_queryset(self):
        # Получаем все компании, связанные с текущим пользователем
        return CompanyUser .objects.filter(user=self.request.user)

# Create your views here.
# при создании компании надо создавать запись в таблице CompanyUser