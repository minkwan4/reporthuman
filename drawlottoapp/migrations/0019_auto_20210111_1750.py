# Generated by Django 3.1.4 on 2021-01-11 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drawlottoapp', '0018_auto_20210111_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lottonumber',
            name='charpoint',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='lottonumber',
            name='수',
            field=models.IntegerField(null=True),
        ),
    ]
