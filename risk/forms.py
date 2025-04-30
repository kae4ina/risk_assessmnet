from django import forms

from assets.models import Asset
from company.models import Company, CompanyUser
from risk.models import Risk, RiskDecision
from threat.models import UserThreat, CompanyThreat
from vulnerability.models import UserVulnerability


class RiskForm(forms.ModelForm):
    related_threats = forms.ModelMultipleChoiceField(queryset=UserThreat.objects.none(), required=False)
    related_vulnerabilities = forms.ModelMultipleChoiceField(queryset=UserVulnerability.objects.none(), required=False)

    class Meta:
        model = Risk
        fields = ['name', 'decision', 'related_company', 'related_threats', 'related_vulnerabilities']
        labels = {
            "name": "Название риска",
            "decision": "Решение",
            "related_company": "Компания"
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(RiskForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['related_company'].queryset = Company.objects.filter(companyuser__user=user)
        else:
            self.fields['related_company'].queryset = Company.objects.none()

        if 'related_company' in self.data:
            try:
                company_id = int(self.data.get('related_company'))
                if 'related_asset' in self.data:
                    asset_id = int(self.data.get('related_asset'))
                    self.fields['related_threats'].queryset = UserThreat.objects.filter(related_asset_id=asset_id)
                    self.fields['related_vulnerabilities'].queryset = UserVulnerability.objects.filter(related_asset_id=asset_id)
            except (ValueError, TypeError):
                pass
        else:
            self.fields['related_threats'].queryset = UserThreat.objects.none()
            self.fields['related_vulnerabilities'].queryset = UserVulnerability.objects.none()




