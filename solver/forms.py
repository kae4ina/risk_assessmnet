from django import forms
from .models import GeneralObjects, GeneralThreats, UserRisk


class RiskCreationForm(forms.ModelForm):
    general_object = forms.ModelChoiceField(
        queryset=GeneralObjects.objects.all(),
        label="Объект защиты"
    )

    threats = forms.ModelMultipleChoiceField(
        queryset=GeneralThreats.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Угрозы"
    )

    class Meta:
        model = UserRisk
        fields = ['general_object']