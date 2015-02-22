# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_but'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='but',
        ),
        migrations.AlterField(
            model_name='news',
            name='posted_date',
            field=models.DateTimeField(verbose_name=b'Data dodania'),
            preserve_default=True,
        ),
    ]
