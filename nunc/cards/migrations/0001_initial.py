# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\uc0dd\uc131\uc77c', auto_now_add=True)),
                ('name', models.CharField(max_length=30, verbose_name='\uce74\ub4dc \uc774\ub984')),
                ('desc', models.CharField(max_length=150, verbose_name='\uce74\ub4dc \uc124\uba85')),
                ('like_count', models.IntegerField(default=0, help_text='\uc88b\uc544\uc694 \uac2f\uc218')),
                ('is_public', models.BooleanField(default=True, help_text='\uce74\ub4dc\uad8c\ud55c')),
                ('users', models.ManyToManyField(help_text='\uc0ac\uc6a9\uc790', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': '\uce74\ub4dc',
                'verbose_name_plural': '\uce74\ub4dc',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\uc0dd\uc131\uc77c', auto_now_add=True)),
                ('title', models.CharField(help_text='\uc2e4\uc81c \uc601\uc0c1 \uc81c\ubaa9', max_length=100)),
                ('query', models.CharField(help_text='\uc0ac\uc6a9\uc790 \ucffc\ub9ac', max_length=100)),
                ('key', models.CharField(help_text='\uc720\ud22c\ube0c \ud0a4', max_length=30)),
                ('image_url', models.CharField(help_text='\uc774\ubbf8\uc9c0 url', max_length=120)),
                ('card', models.ForeignKey(help_text='\uc18d\ud55c\uce74\ub4dc', to='cards.Card')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': '\uc601\uc0c1',
                'verbose_name_plural': '\uc601\uc0c1',
            },
            bases=(models.Model,),
        ),
    ]
