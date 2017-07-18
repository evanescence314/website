# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contest', '0004_auto_20170711_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isCorrect', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-question', '-user'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.IntegerField()),
            ],
            options={
                'ordering': ['-contest', '-num'],
            },
        ),
        migrations.AddField(
            model_name='contest',
            name='isWeighted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contest',
            name='num_quest',
            field=models.IntegerField(default=6),
        ),
        migrations.AddField(
            model_name='question',
            name='contest',
            field=models.ForeignKey(to='contest.Contest'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='contest.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
