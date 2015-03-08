# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='image_url_high',
            field=models.CharField(default=datetime.datetime(2015, 3, 4, 19, 41, 47, 761851, tzinfo=utc), help_text='\uc774\ubbf8\uc9c0 url high', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='image_url_medium',
            field=models.CharField(default=datetime.datetime(2015, 3, 4, 19, 41, 53, 514343, tzinfo=utc), help_text='\uc774\ubbf8\uc9c0 url medium', max_length=120),
            preserve_default=False,
        ),
    ]
