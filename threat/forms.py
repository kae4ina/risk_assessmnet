from django import forms

from assets.models import Asset
from company.models import Company, CompanyUser
from .models import UserThreat

class UserThreatForm(forms.ModelForm):
    company = forms.ModelChoiceField(queryset=Company.objects.none(), required=True)
   # related_assets = forms.ModelMultipleChoiceField(queryset=Asset.objects.none(), required=True)

    class Meta:
        model = UserThreat
        fields = ['name', 'company', 'possibility', 'related_asset']
        labels={
            "name":"Название угрозы",
            "company": "Компания",
            "possibility": "Вероятность реализации угрозы",
            "related_asset": "Связанные активы",

        }


    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Извлекаем user из kwargs
        super(UserThreatForm, self).__init__(*args, **kwargs)

        if user:
            # Получаем queryset для поля company как объекты Company
            self.fields['company'].queryset = CompanyUser.objects.filter(user=user).select_related(
                'company').values_list('company', flat=True)

            # Теперь получаем реальные объекты Company
            self.fields['company'].queryset = Company.objects.filter(id__in=self.fields['company'].queryset)

            # Активы для поля related_asset, которые будут привязаны к создаваемой UserThreat
            self.fields['related_asset'].queryset = Asset.objects.filter(company__in=self.fields['company'].queryset)