from django.db import models


class DefaultAssetCategory(models.Model):
    default_asset_category = models.CharField(max_length=100)

    def __str__(self):
        return self.default_asset_category


class DefaultAssetValue(models.Model):
    default_asset_value = models.CharField(max_length=100)

    def __str__(self):
        return self.default_asset_value


class DefaultAssetType(models.Model):  # Убедитесь, что у вас есть эта модель
    default_asset_type = models.CharField(max_length=100)

    def __str__(self):
        return self.default_asset_type


class DefaultAssetModel(models.Model):
    name = models.CharField(max_length=255, null=True)
    #id устанавливается сам по умолчанию
    #тип актива - это DefaultAssetEnum,
    #категория - это DefaultAssetCategory (информаионные, физические,программные, услуги, персонал или нематериальные ценности)
    default_asset_type = models.ForeignKey(DefaultAssetType, on_delete=models.CASCADE)
    default_asset_category = models.ForeignKey(DefaultAssetCategory, on_delete=models.CASCADE)
    default_asset_value = models.ForeignKey(DefaultAssetValue, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



