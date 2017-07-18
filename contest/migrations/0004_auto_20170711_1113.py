# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('contest', '0003_auto_20151016_0147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
            ],
            options={
                'ordering': ['last_name', 'first_name'],
                'proxy': True,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterModelOptions(
            name='contest',
            options={'ordering': ['-date', '-block']},
        ),
        migrations.AlterModelOptions(
            name='score',
            options={'ordering': ['user']},
        ),
        migrations.AlterField(
            model_name='score',
            name='user',
            field=models.ForeignKey(to='contest.Student'),
        ),
        migrations.AlterUniqueTogether(
            name='score',
            unique_together=set([('user', 'contest')]),
        ),
    ]
