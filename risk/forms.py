from django import forms

from company.models import Company
from risk.models import Risk


class RiskForm(forms.ModelForm):

    class Meta:
        model = Risk
        fields = ['name','exploit_possibility', 'related_threat','related_company']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Извлекаем пользователя из kwargs
        super(RiskForm, self).__init__(*args, **kwargs)
        if user is not None:
            self.fields['related_company'].queryset = Company.objects.filter(companyuser__user=user)

    """ def clean_exploit_possibility(self):
            value = self.cleaned_data.get('exploit_possibility')
            if value < 0:
                raise forms.ValidationError("Значение не может быть меньше 0.")
            return value
    """