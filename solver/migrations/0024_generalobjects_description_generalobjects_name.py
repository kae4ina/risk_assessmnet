# Generated by Django 5.1.1 on 2025-03-31 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solver', '0023_remove_generalobjects_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalobjects',
            name='description',
            field=models.CharField(default='kbh', max_length=700),
        ),
        migrations.AddField(
            model_name='generalobjects',
            name='name',
            field=models.CharField(default='kbh', max_length=200),
        ),
    ]
