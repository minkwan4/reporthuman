# Generated by Django 3.1.4 on 2021-01-11 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drawlottoapp', '0019_auto_20210111_1750'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lottonumber',
            old_name='수',
            new_name='charpoint_instance',
        ),
    ]
