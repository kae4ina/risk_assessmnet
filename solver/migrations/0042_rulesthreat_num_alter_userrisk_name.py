# Generated by Django 5.1.1 on 2025-04-08 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solver', '0041_userrisk_name_alter_userrisk_money_loss'),
    ]

    operations = [
        migrations.AddField(
            model_name='rulesthreat',
            name='num',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AlterField(
            model_name='userrisk',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
