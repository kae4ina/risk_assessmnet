from django import forms

from company.models import CompanyUser
from risk.models import Risk
from threat.models import UserThreat


class RiskForm(forms.ModelForm):
    company = forms.ModelChoiceField(queryset=CompanyUser .objects.none(), required=True)
    related_threat = forms.ModelChoiceField(queryset=UserThreat.objects.none(), required=True)

    class Meta:
        model = Risk
        fields = ['name', 'exploit_possibility', 'company', 'related_threat']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(RiskForm, self).__init__(*args, **kwargs)
        if user:

            self.fields['company'].queryset = CompanyUser .objects.filter(user=user)

            if 'company' in self.data:
                try:
                    company_id = int(self.data.get('company'))
                    self.fields['related_threat'].queryset = UserThreat.objects.filter(related_asset__company_id=company_id)
                except (ValueError, TypeError):
                    pass
            elif self.instance.pk:
                self.fields['related_threat'].queryset = self.instance.company.userthreat_set.all()
