from django import forms

from company.models import Company, DefaultCompanyArea, CompanyUser


class CompanyForm(forms.ModelForm):
    class Meta:
        model=Company
        fields=['company_name','default_company_area']


        default_company_area=forms.ModelChoiceField(queryset=DefaultCompanyArea.objects.all())



