# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('himapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='category',
        ),
        migrations.AddField(
            model_name='company',
            name='subcategory',
            field=models.ForeignKey(default=None, to='himapp.Subcategory'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='pincode',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='company',
            name='slug',
            field=models.SlugField(unique=True, max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='type',
            field=models.CharField(max_length=25, choices=[(b'public', b'Public'), (b'private', b'Private')]),
        ),
    ]
