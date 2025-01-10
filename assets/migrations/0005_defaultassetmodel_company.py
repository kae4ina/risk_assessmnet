# Generated by Django 5.1.1 on 2025-01-10 04:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_rename_defaultassetenum_defaultassettype_and_more'),
        ('company', '0004_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='defaultassetmodel',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='company.company'),
        ),
    ]
