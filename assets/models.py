from django.db import models

class DefaultAssetCategory(models.Model):
    default_asset_category = models.CharField(max_length=100)
    def __str__(self):
        return self.default_asset_category

class DefaultAssetValue(models.Model):
    default_asset_value=models.CharField(max_length=100)
    def __str__(self):
        return self.default_asset_value
# Create your models here.
class DefaultAssetEnum(models.Model):
    default_asset_element=models.CharField(max_length=100)
    def __str__(self):
        return self.default_asset_element

class DefaultAssetModel(models.Model):
    #id устанавливается сам по умолчанию
    default_asset_name=models.ForeignKey(to=DefaultAssetEnum, on_delete= models.CASCADE)
    default_asset_category=models.ForeignKey(to=DefaultAssetCategory, on_delete= models.CASCADE)
    default_asset_value=models.ForeignKey(to=DefaultAssetValue, on_delete= models.CASCADE)

