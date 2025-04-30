from django.db import models
from django.db.models import CASCADE

from company.models import Company


class DefaultAssetCategory(models.Model):
    default_asset_category = models.CharField(max_length=100,verbose_name="Категория актива")

    def __str__(self):
        return self.default_asset_category


class DefaultAssetValue(models.Model):
    default_asset_value = models.CharField(max_length=100,verbose_name="Значимость актива")

    def __str__(self):
        return self.default_asset_value


class DefaultAssetType(models.Model):
    default_asset_type = models.CharField(max_length=100,verbose_name="Тип актива")

    def __str__(self):
        return self.default_asset_type


class Asset(models.Model):
    name = models.CharField(max_length=255, null=True)
    #id устанавливается сам по умолчанию
    #тип актива - это DefaultAssetEnum,
    #категория - это DefaultAssetCategory (информаионные, физические,программные, услуги, персонал или нематериальные ценности)
    default_asset_type = models.ForeignKey(DefaultAssetType, on_delete=models.CASCADE)
    default_asset_category = models.ForeignKey(DefaultAssetCategory, on_delete=models.CASCADE)
    default_asset_value = models.ForeignKey(DefaultAssetValue, on_delete=models.CASCADE)
    company=models.ForeignKey(Company,related_name='assets',on_delete=CASCADE) # получить все активы компании - company.assets.all()

    def __str__(self):
        return self.name





