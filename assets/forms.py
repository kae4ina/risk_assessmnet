from django import forms

from assets.Asset import Asset
from assets.models import DefaultAssetEnum, DefaultAssetCategory, DefaultAssetValue, DefaultAssetModel


class AssetForm(forms.ModelForm):
    class Meta:
        model = DefaultAssetModel
        fields = ['default_asset_name', 'default_asset_category', 'default_asset_value']
        default_asset_name = forms.ModelChoiceField(queryset=DefaultAssetEnum.objects.all())
        default_asset_category = forms.ModelChoiceField(queryset=DefaultAssetCategory.objects.all())
        default_asset_value = forms.ModelChoiceField(queryset=DefaultAssetValue.objects.all())