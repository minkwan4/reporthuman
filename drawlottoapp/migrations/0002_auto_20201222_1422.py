# Generated by Django 3.1.4 on 2020-12-22 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drawlottoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lottonumber',
            name='text',
            field=models.IntegerField(),
        ),
    ]
