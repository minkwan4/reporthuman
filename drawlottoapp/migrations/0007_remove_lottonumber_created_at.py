# Generated by Django 3.1.4 on 2020-12-28 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drawlottoapp', '0006_auto_20201228_0818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lottonumber',
            name='created_at',
        ),
    ]