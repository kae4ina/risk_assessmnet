# Generated by Django 5.1.1 on 2025-04-08 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solver', '0039_alter_userrisk_ways'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrisk',
            name='money_loss',
            field=models.FloatField(default=1000),
        ),
    ]
