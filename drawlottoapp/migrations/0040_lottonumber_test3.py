# Generated by Django 3.1.4 on 2021-01-24 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drawlottoapp', '0039_lottonumber_test2'),
    ]

    operations = [
        migrations.AddField(
            model_name='lottonumber',
            name='test3',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
