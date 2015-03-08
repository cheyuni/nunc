# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='facebook_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='user',
            name='status',
        ),
    ]
