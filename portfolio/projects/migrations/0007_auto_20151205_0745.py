# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_mainimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='mainimage',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
