# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('gender', models.BooleanField(default=True, help_text='\uc131\ubcc4')),
                ('birthday', models.DateField(null=True, blank=True)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name='Email', db_index=True)),
                ('phone_number', models.CharField(max_length=20, null=True, verbose_name='\uc804\ud654\ubc88\ud638 (ID)')),
                ('user_name', models.CharField(help_text='\uc0ac\uc6a9\uc790 \uc774\ub984', max_length=255, verbose_name='\uc0ac\uc6a9\uc790 \uc774\ub984')),
            ],
            options={
                'verbose_name': '\uc0ac\uc6a9\uc790',
                'verbose_name_plural': '\uc0ac\uc6a9\uc790\ub4e4',
            },
            bases=(models.Model,),
        ),
    ]
