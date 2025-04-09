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

    ways = forms.CharField(
        widget=forms.HiddenInput(),
        required=False
    )

    name = forms.CharField(
        label="Название риска",
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    money_loss = forms.FloatField(
        label="Возможные потери (руб)",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'})
    )

    class Meta:
        model = UserRisk
        fields = ['name', 'general_object', 'threats', 'ways', 'money_loss']