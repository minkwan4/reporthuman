# Generated by Django 3.1.4 on 2020-12-26 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drawlottoapp', '0003_auto_20201222_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='lottonumber',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]