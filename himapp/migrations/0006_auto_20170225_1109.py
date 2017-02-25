# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('himapp', '0005_auto_20170225_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(max_length=100),
        ),
    ]
