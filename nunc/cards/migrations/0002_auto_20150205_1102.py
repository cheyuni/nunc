# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='user',
            new_name='card',
        ),
        migrations.RemoveField(
            model_name='card',
            name='user',
        ),
        migrations.AddField(
            model_name='card',
            name='users',
            field=models.ManyToManyField(help_text='\uc0ac\uc6a9\uc790', to='users.User'),
            preserve_default=True,
        ),
    ]
