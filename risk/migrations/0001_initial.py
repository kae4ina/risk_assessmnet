# Generated by Django 5.1.1 on 2025-01-24 10:29

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('threat', '0002_remove_userthreat_related_assets_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('exploit_possibility', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
                ('related_threat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='threat.userthreat')),
            ],
        ),
    ]
