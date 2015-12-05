# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20151202_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 3, 2, 54, 11, 385600, tzinfo=utc), verbose_name='date published'),
            preserve_default=False,
        ),
    ]
