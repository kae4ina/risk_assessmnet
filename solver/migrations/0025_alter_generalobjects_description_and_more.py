# Generated by Django 5.1.1 on 2025-03-31 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solver', '0024_generalobjects_description_generalobjects_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalobjects',
            name='description',
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name='generalobjects',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
