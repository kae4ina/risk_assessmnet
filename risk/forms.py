from django import forms

from risk.models import Risk


class RiskForm(forms.ModelForm):

    class Meta:
        model = Risk
        fields = ['name', 'exploit_possability', 'related_threat']

    def clean_exploit_possability(self):
        value = self.cleaned_data.get('exploit_possability')
        if value < 0:
            raise forms.ValidationError("Значение не может быть меньше 0.")
        return value