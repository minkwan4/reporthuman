# Generated by Django 3.1.4 on 2021-01-24 09:46

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drawlottoapp', '0033_auto_20210122_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultlotto',
            name='result',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=7),
        ),
    ]
