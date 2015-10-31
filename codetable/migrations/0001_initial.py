# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=20000)),
                ('lang', models.CharField(default=b'C', max_length=20)),
                ('hash', models.CharField(max_length=20)),
                ('published_date', models.DateTimeField(blank=True)),
            ],
        ),
    ]
