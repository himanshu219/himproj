# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100, blank=True)),
                ('show_on_site', models.BooleanField(default=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100, blank=True)),
                ('show_on_site', models.BooleanField(default=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cin', models.CharField(unique=True, max_length=25)),
                ('company_name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('status', models.IntegerField(choices=[(1, b'Active'), (2, b'InActive')])),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('type', models.CharField(max_length=25, choices=[(1, b'Public'), (2, b'Private')])),
                ('authorised_capital', models.DecimalField(default=0.0, max_digits=15, decimal_places=2)),
                ('paidup_capital', models.DecimalField(default=0.0, max_digits=15, decimal_places=2)),
                ('incorporation_date', models.DateField()),
                ('agm_date', models.DateField()),
                ('balancesheet_date', models.DateField()),
                ('address1', models.TextField(null=True, blank=True)),
                ('address2', models.TextField(null=True, blank=True)),
                ('full_address', models.TextField(null=True, blank=True)),
                ('pincode', models.PositiveIntegerField(validators=[django.core.validators.MaxLengthValidator(6), django.core.validators.MinLengthValidator(6)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100, blank=True)),
                ('show_on_site', models.BooleanField(default=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100, blank=True)),
                ('show_on_site', models.BooleanField(default=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('din', models.CharField(unique=True, max_length=25)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DirectorCompany',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('designation', models.CharField(max_length=50)),
                ('appointment_date', models.DateField()),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('company', models.ForeignKey(to='himapp.Company')),
                ('director', models.ForeignKey(to='himapp.Director')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100, blank=True)),
                ('show_on_site', models.BooleanField(default=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('country', models.ForeignKey(to='himapp.Country')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100, blank=True)),
                ('show_on_site', models.BooleanField(default=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.ForeignKey(to='himapp.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='company',
            name='alldirectors',
            field=models.ManyToManyField(to='himapp.Director', through='himapp.DirectorCompany'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='category',
            field=models.ForeignKey(to='himapp.Category'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='city',
            field=models.ForeignKey(to='himapp.City'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(to='himapp.Country'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(blank=True, to='himapp.State', null=True),
            preserve_default=True,
        ),
    ]
