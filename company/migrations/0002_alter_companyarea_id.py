# Generated by Django 5.1.1 on 2024-11-07 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyarea',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
