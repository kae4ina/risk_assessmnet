# Generated by Django 5.1.2 on 2025-04-30 19:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_alter_companyuser_user'),
        ('task', '0007_alter_task_user_risk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='company',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='company.company'),
        ),
    ]
