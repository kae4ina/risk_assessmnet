from django import forms

from company.models import CompanyUser, Company
from measure.models import UserMeasure
from risk.models import Risk
from solver.models import UserRisk


class UserMeasureForm(forms.ModelForm):
    class Meta:
        model = UserMeasure
        fields = ['name', 'description', 'related_company', 'related_risk']
        labels = {
            "name": "Мера",
            "description": "Описание",
            "related_risk": "Связанный риск",
            "related_company": "Компания"
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(UserMeasureForm, self).__init__(*args, **kwargs)

        if user:
            # Ограничиваем компании только теми, к которым имеет доступ пользователь
            user_companies = CompanyUser.objects.filter(user=user).values_list('company', flat=True)
            self.fields['related_company'].queryset = Company.objects.filter(id__in=user_companies)

            # Изначально пустой queryset для рисков
            self.fields['related_risk'].queryset = UserRisk.objects.none()
        else:
            self.fields['related_company'].queryset = Company.objects.none()
            self.fields['related_risk'].queryset = UserRisk.objects.none()

        self.fields['description'].widget = forms.Textarea(attrs={'rows': 4, 'cols': 40})