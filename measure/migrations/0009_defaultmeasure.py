# Generated by Django 5.1.1 on 2025-03-24 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measure', '0008_delete_defaultmeasure'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultMeasure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
    ]
