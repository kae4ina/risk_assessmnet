from django import forms

from company.models import CompanyUser, Company
from measure.models import UserMeasure
from risk.models import Risk


class UserMeasureForm(forms.ModelForm):
    class Meta:
        model=UserMeasure
        fields=['name','description','related_risk', 'related_company']
        labels={
            "name":"Мера",
            "description": "Описание",
            "related_risk": "Связанный риск",
            "related_company": "Компания"
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(UserMeasureForm, self).__init__(*args, **kwargs)

        if user:

            user_companies = CompanyUser.objects.filter(user=user).values_list('company', flat=True)


            self.fields['related_company'].queryset = Company.objects.filter(id__in=user_companies)


            # риски по компаниям пользователя
            self.fields['related_risk'].queryset = Risk.objects.filter(related_company__in=user_companies)
        else:
            self.fields['related_company'].queryset = Company.objects.none()
            self.fields['related_risk'].queryset = Risk.objects.none()

        self.fields['description'].widget = forms.Textarea(attrs={'rows': 4, 'cols': 40})