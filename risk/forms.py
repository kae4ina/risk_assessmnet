from django import forms

from company.models import Company
from risk.models import Risk, RiskDecision


class RiskForm(forms.ModelForm):

    class Meta:
        model = Risk
        fields = ['name', 'related_threat','decision', 'related_company']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(RiskForm, self).__init__(*args, **kwargs)
        self.fields['decision'].queryset = RiskDecision.objects.all()




