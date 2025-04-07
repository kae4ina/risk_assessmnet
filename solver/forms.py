from django import forms
from .models import GeneralObjects, GeneralThreats, UserRisk, Ways

from django import forms
from .models import UserRisk, GeneralObjects, GeneralThreats, ThreatWays


class RiskCreationForm(forms.ModelForm):
    general_object = forms.ModelChoiceField(
        queryset=GeneralObjects.objects.all(),
        label="Объект защиты",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    threats = forms.ModelMultipleChoiceField(
        queryset=GeneralThreats.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Угрозы"
    )

    ways = forms.ModelMultipleChoiceField(
        queryset=Ways.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control d-none'}),
        label="Способы реализации",
        required=False
    )

    class Meta:
        model = UserRisk
        fields = ['general_object', 'threats', 'ways']