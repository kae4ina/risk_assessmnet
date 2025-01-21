from django import forms

#from assets.Asset import Asset
from assets.models import DefaultAssetType, DefaultAssetCategory, DefaultAssetValue, Asset
from company.models import Company


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['name', 'default_asset_type', 'default_asset_category', 'default_asset_value','company']



    default_asset_type = forms.ModelChoiceField(queryset=DefaultAssetType.objects.all())
    default_asset_category = forms.ModelChoiceField(queryset=DefaultAssetCategory.objects.all())
    default_asset_value = forms.ModelChoiceField(queryset=DefaultAssetValue.objects.all())

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Извлекаем пользователя из kwargs
        super(AssetForm, self).__init__(*args, **kwargs)
        if user is not None:
            self.fields['company'].queryset = Company.objects.filter(companyuser__user=user)
