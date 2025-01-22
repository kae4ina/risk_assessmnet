from django import forms

from assets.models import Asset
from company.models import Company
from .models import UserThreat

class UserThreatForm(forms.ModelForm):
    company = forms.ModelChoiceField(queryset=Company.objects.none(), required=True)
    related_assets = forms.ModelMultipleChoiceField(queryset=Asset.objects.none(), required=True)

    class Meta:
        model = UserThreat
        fields = ['name', 'company', 'related_assets']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(UserThreatForm, self).__init__(*args, **kwargs)
        if user:
            # Получаем компании, связанные с пользователем
            self.fields['company'].queryset = Company.objects.filter(companyuser__user=user)
            if 'company' in self.data:
                try:
                    company_id = int(self.data.get('company'))
                    self.fields['related_assets'].queryset = Asset.objects.filter(company_id=company_id)
                except (ValueError, TypeError):
                    pass  # Если не удалось получить id компании
            elif self.instance.pk:
                self.fields['related_assets'].queryset = self.instance.related_assets.all()
