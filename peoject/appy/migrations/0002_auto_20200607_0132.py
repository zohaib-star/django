# Generated by Django 3.0.6 on 2020-06-07 08:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('appy', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='b',
            old_name='fst',
            new_name='st',
        ),
        migrations.RemoveField(
            model_name='b',
            name='scd',
        ),
        migrations.AddField(
            model_name='a',
            name='start',
            field=models.DateField(default=datetime.datetime(2020, 6, 7, 8, 32, 20, 295817, tzinfo=utc), verbose_name='since'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='b',
            name='cd',
            field=models.BooleanField(default=False),
        ),
    ]