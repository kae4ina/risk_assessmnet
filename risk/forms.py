from django import forms

from assets.models import Asset
from company.models import Company, CompanyUser
from risk.models import Risk, RiskDecision
from threat.models import UserThreat, CompanyThreat
from vulnerability.models import UserVulnerability


class RiskForm(forms.ModelForm):

    class Meta:
        model = Risk
        fields = ['name', 'related_threat','decision','related_vulnerability', 'related_company']
        labels={
            "name":"Название риска",
            "decision": "Решение",
            "related_company": "Компания"

        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Получаем пользователя из kwargs
        super(RiskForm, self).__init__(*args, **kwargs)

        # Фильтруем компании по пользователю
        if user:
            self.fields['related_company'].queryset = Company.objects.filter(companyuser__user=user)
        else:
            self.fields[
                'related_company'].queryset = Company.objects.none()  # Если пользователь не передан, пустой queryset

        # Изначально пустые списки для угроз и уязвимостей
        self.fields['related_threat'].queryset = UserThreat.objects.none()
        self.fields['related_vulnerability'].queryset = UserVulnerability.objects.none()

        if 'related_company' in self.data:
            try:
                company_id = int(self.data.get('related_company'))
                # Получаем активы, связанные с выбранной компанией
                assets = Asset.objects.filter(company_id=company_id)
                # Если актив был выбран, обновляем угрозы и уязвимости
                if 'related_asset' in self.data:
                    asset_id = int(self.data.get('related_asset'))
                    self.fields['related_threat'].queryset = UserThreat.objects.filter(related_asset_id=asset_id)
                    self.fields['related_vulnerability'].queryset = UserVulnerability.objects.filter(
                        related_asset_id=asset_id)
            except (ValueError, TypeError):
                pass  # Игнорируем ошибки, если данные некорректны
        else:
            # Если компания не выбрана, оставляем пустыми
            self.fields['related_threat'].queryset = UserThreat.objects.none()
            self.fields['related_vulnerability'].queryset = UserVulnerability.objects.none()



