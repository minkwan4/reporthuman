# Generated by Django 3.1.4 on 2021-01-16 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drawlottoapp', '0029_auto_20210116_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lottonumber',
            name='charpoint',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='lottonumber',
            name='charpoint_instance',
            field=models.IntegerField(default=2, null=True),
        ),
    ]
