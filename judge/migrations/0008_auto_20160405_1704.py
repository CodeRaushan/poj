# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-05 17:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0007_auto_20160405_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='problem',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='judge.Problem'),
        ),
        migrations.AlterField(
            model_name='unevaluatedsubmission',
            name='problem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='judge.Problem'),
        ),
        migrations.AlterField(
            model_name='unevaluatedsubmission',
            name='submitter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='judge.Coder'),
        ),
    ]