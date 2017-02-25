# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('himapp', '0003_auto_20170225_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=models.SlugField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='slug',
            field=models.SlugField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='director',
            name='slug',
            field=models.SlugField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='slug',
            field=models.SlugField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(max_length=100, blank=True),
        ),
    ]
