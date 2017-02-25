# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('himapp', '0004_auto_20170225_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='slug',
            field=models.SlugField(max_length=100, blank=True),
        ),
    ]
