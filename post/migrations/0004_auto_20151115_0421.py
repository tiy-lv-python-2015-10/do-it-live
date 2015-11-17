# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='User',
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='post',
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]
