# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20151205_0546'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='mainimage',
            field=models.ImageField(default='./BasedGod_8pRBy1v.png', upload_to='./images'),
            preserve_default=False,
        ),
    ]
