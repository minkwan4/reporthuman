# Generated by Django 3.1.4 on 2021-01-11 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drawlottoapp', '0010_auto_20201228_0831'),
    ]

    operations = [
        migrations.AddField(
            model_name='lottonumber',
            name='lottocount',
            field=models.IntegerField(null=True),
        ),
    ]