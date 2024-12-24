from django.db import models

class Asset(models.Model):
    # Определяем перечисление для asset_value
    class AssetValue(models.TextChoices):
        VALUE_1 = 'high_relevant', 'Очень важные'
        VALUE_2 = 'relevant', 'Важные'
        VALUE_3 = 'low_relevant', 'Не очень важные'
        VALUE_4 = 'non_relevant', 'Неважные'
    class AsseType(models.TextChoices):
        VALUE_1 = 'material', 'Материальные'
        VALUE_2 = 'intangible', 'Нематериальные'
    class AssetName(models.TextChoices):
        VALUE_1 = 'IS', 'ИС'
        VALUE_2 = 'data', 'Данные'
        VALUE_3 = 'infrastructure', 'Инфраструктура'
        VALUE_4 = 'network', 'Сеть'
        VALUE_5 = 'products', 'Продукты'

    asset_id = models.CharField(max_length=100, unique=True)
    asset_name = models.CharField(
        max_length=255,
        choices=AssetName.choices,  # Используем перечисление для выбора
        default=AssetName.VALUE_1
                                  )
    asset_value = models.CharField(
        max_length=20,
        choices=AssetValue.choices,  # Используем перечисление для выбора
        default=AssetValue.VALUE_4,   # Устанавливаем значение по умолчанию - неважный актив
    )
    asset_type=models.CharField(
        max_length=20,
        choices=AsseType.choices,
        default=AsseType.VALUE_1,#по умолчанию материальный актив
    )



