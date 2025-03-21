# Generated by Django 5.1.1 on 2025-03-18 06:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('measure', '0006_defaultmeasure'),
        ('threat', '0012_alter_userthreat_possibility'),
        ('vulnerability', '0015_defaultvulnerability_related_asset_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RulesThreat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measure.defaultmeasure')),
                ('threat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='threat.defaultthreat')),
            ],
        ),
        migrations.CreateModel(
            name='RulesVuln',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measure.defaultmeasure')),
                ('vuln', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vulnerability.defaultvulnerability')),
            ],
        ),
    ]
