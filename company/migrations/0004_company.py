# Generated by Django 5.1.1 on 2024-11-07 07:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_defaultcompanyarea_delete_companyarea'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('default_company_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.defaultcompanyarea')),
            ],
        ),
    ]
