# Generated by Django 5.1.1 on 2025-03-31 10:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solver', '0026_remove_threatobject_id_generalthreat'),
    ]

    operations = [
        migrations.AddField(
            model_name='threatobject',
            name='id_generalthreat',
            field=models.ForeignKey(default='g', on_delete=django.db.models.deletion.CASCADE, to='solver.generalthreats'),
        ),
    ]
