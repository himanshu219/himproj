# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('himapp', '0002_auto_20170225_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='agm_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='balancesheet_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='pincode',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='status',
            field=models.CharField(max_length=25, choices=[(b'Active', b'Active'), (b'InActive', b'InActive')]),
        ),
        migrations.AlterField(
            model_name='company',
            name='type',
            field=models.CharField(max_length=25, choices=[(b'Public', b'Public'), (b'Private', b'Private')]),
        ),
    ]
