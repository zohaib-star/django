# Generated by Django 3.0.6 on 2020-06-07 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appy', '0002_auto_20200607_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='a',
            name='start',
            field=models.DateTimeField(verbose_name='since'),
        ),
    ]