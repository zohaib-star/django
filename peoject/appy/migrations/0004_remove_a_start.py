# Generated by Django 3.0.6 on 2020-06-07 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appy', '0003_auto_20200607_0148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='a',
            name='start',
        ),
    ]
