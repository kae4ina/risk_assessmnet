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
        form_company=CompanyForm(request.POST)
        if form_company.is_valid():
            company=form_company.save()
            company_user=CompanyUser(company=company, user=request.user)
            company_user.save()
            return redirect('company_saved')
    else:
        form_company = CompanyForm()



    return render(request, 'company/company_create.html', {'form': form_company})

def company_saved(request):
    return render(request,'company/company_saved.html')



class UserCompaniesView(LoginRequiredMixin, ListView):
    model = CompanyUser
    template_name = 'accounts/user_companies.html'
    context_object_name = 'company_users'  

    def get_queryset(self):
        # Получаем все компании, связанные с текущим пользователем
        return CompanyUser .objects.filter(user=self.request.user)

# Create your views here.
# при создании компании надо создавать запись в таблице CompanyUser