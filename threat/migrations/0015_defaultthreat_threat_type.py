# Generated by Django 5.1.1 on 2025-03-18 07:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threat', '0014_alter_threattype_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='defaultthreat',
            name='threat_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='threat.threattype'),
        ),
    ]
