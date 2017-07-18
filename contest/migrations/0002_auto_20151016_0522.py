# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='block',
            field=models.IntegerField(choices=[(1, 'A'), (2, 'B'), (3, 'Both')]),
        ),
    ]
