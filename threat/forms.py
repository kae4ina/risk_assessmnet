from django import forms

from assets.models import Asset
from company.models import Company, CompanyUser
from .models import UserThreat

class UserThreatForm(forms.ModelForm):
    company = forms.ModelChoiceField(queryset=Company.objects.none(), required=True)
    related_assets = forms.ModelMultipleChoiceField(
        queryset=Asset.objects.none(),
        required=True,
        widget=forms.CheckboxSelectMultiple  # Используем CheckboxSelectMultiple для множественного выбора
    )

    class Meta:
        model = UserThreat
        fields = ['name', 'company', 'possibility', 'related_assets']
        labels = {
            "name": "Название угрозы",
            "company": "Компания",
            "possibility": "Вероятность реализации угрозы",
            "related_assets": "Связанные активы",
        }


    def __init__(self, *args, **kwargs):
        super(UserThreatForm, self).__init__(*args, **kwargs)
        user = kwargs['initial'].get('user')
        if user:
            self.fields['company'].queryset = CompanyUser.objects.filter(user=user).select_related(
                'company').values_list('company', flat=True)
            self.fields['company'].queryset = Company.objects.filter(id__in=self.fields['company'].queryset)

            if 'company' in self.data:
                try:
                    company_id = int(self.data.get('company'))
                    self.fields['related_assets'].queryset = Asset.objects.filter(company_id=company_id)
                except (ValueError, TypeError):
                    pass  # Если не удалось получить company_id, оставляем пустым
            else:  # Если форма не отправлена, оставляем пустым
                self.fields['related_assets'].queryset = Asset.objects.none()
