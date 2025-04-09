# Generated by Django 5.1.1 on 2025-04-09 04:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solver', '0047_delete_rulesthreat'),
    ]

    operations = [
        migrations.CreateModel(
            name='RulesThreat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=4)),
                ('measure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solver.defaultmeasure')),
                ('threat', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='solver.generalthreats')),
            ],
        ),
    ]
