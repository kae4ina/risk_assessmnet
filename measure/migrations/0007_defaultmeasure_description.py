# Generated by Django 5.1.1 on 2025-03-18 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measure', '0006_defaultmeasure'),
    ]

    operations = [
        migrations.AddField(
            model_name='defaultmeasure',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
