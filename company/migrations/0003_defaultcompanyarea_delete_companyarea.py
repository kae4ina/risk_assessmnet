# Generated by Django 5.1.1 on 2024-11-07 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_alter_companyarea_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultCompanyArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_company_area', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='CompanyArea',
        ),
    ]
