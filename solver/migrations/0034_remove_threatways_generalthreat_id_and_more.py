# Generated by Django 5.1.1 on 2025-04-01 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solver', '0033_rename_generalthreat_threatways_generalthreat_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='threatways',
            name='generalthreat_id',
        ),
        migrations.RemoveField(
            model_name='threatways',
            name='way_id',
        ),
    ]
