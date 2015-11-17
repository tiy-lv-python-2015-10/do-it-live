# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_users'),
        ('post', '0002_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('User', models.ForeignKey(to='user.Users')),
                ('post', models.ForeignKey(to='post.Post')),
            ],
        ),
    ]
