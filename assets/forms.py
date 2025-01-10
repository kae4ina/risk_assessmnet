from django import forms

from assets.Asset import Asset
from assets.models import DefaultAssetType, DefaultAssetCategory, DefaultAssetValue, DefaultAssetModel


class AssetForm(forms.ModelForm):
    class Meta:
        model = DefaultAssetModel
        fields = ['name', 'default_asset_type', 'default_asset_category', 'default_asset_value']  # Исправлено на правильные поля
        # Добавляем скрытое поле для компании
        company_id = forms.IntegerField(widget=forms.HiddenInput())

    # Поля выбора определены здесь, но они уже включены в `fields`, так что их можно не дублировать

    default_asset_type = forms.ModelChoiceField(queryset=DefaultAssetType.objects.all())
    default_asset_category = forms.ModelChoiceField(queryset=DefaultAssetCategory.objects.all())
    default_asset_value = forms.ModelChoiceField(queryset=DefaultAssetValue.objects.all())
