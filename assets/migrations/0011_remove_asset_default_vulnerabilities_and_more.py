# Generated by Django 5.1.1 on 2025-02-25 07:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0010_remove_asset_default_asset_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='default_vulnerabilities',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='vulnerabilities',
        ),
        migrations.AddField(
            model_name='asset',
            name='default_asset_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='assets.defaultassetcategory'),
        ),
    ]
