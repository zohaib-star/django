# Generated by Django 3.0.6 on 2020-06-07 09:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('appy', '0004_remove_a_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='a',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 7, 9, 26, 49, 46296, tzinfo=utc), verbose_name='since'),
            preserve_default=False,
        ),
    ]
