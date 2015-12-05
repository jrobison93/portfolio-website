# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('project_name', models.CharField(max_length=50)),
                ('short_description', models.CharField(max_length=200)),
                ('long_description', models.CharField(max_length=1000)),
                ('overview_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
