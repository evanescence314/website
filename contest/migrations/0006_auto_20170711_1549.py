# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0005_auto_20170711_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='max_score',
            field=models.IntegerField(default=25),
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(to='contest.Score'),
        ),
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.DecimalField(max_digits=5, decimal_places=3),
        ),
    ]
