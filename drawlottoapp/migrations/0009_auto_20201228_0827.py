# Generated by Django 3.1.4 on 2020-12-28 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drawlottoapp', '0008_lottonumber_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lottonumber',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
