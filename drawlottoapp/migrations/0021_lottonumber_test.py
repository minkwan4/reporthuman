# Generated by Django 3.1.4 on 2021-01-11 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drawlottoapp', '0020_auto_20210111_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='lottonumber',
            name='test',
            field=models.CharField(max_length=255, null=True),
        ),
    ]