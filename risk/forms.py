from django import forms

from assets.models import Asset
from company.models import Company, CompanyUser
from risk.models import Risk, RiskDecision
from threat.models import UserThreat, CompanyThreat


class RiskForm(forms.ModelForm):

    class Meta:
        model = Risk
        fields = ['name', 'related_threat','decision', 'related_company']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(RiskForm, self).__init__(*args, **kwargs)
        self.fields['decision'].queryset = RiskDecision.objects.all()

        if user:
            # Получаем queryset для поля company как объекты Company
            company_ids = CompanyUser.objects.filter(user=user).values_list('company', flat=True)
            self.fields['related_company'].queryset = Company.objects.filter(id__in=company_ids)

            if 'related_company' in self.data:
                try:
                    company_id = int(self.data.get('related_company'))
                    self.fields['related_threat'].queryset = UserThreat.objects.filter(
                        companythreat__company_id=company_id
                    )
                except (ValueError, TypeError):
                    pass  # Если компания не выбрана, оставляем пустым
            else:
                self.fields['related_threat'].queryset = UserThreat.objects.none()




