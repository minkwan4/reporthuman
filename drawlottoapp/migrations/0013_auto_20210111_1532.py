# Generated by Django 3.1.4 on 2021-01-11 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drawlottoapp', '0012_lottonumber_created_at2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lottonumber',
            name='created_at2',
            field=models.DateTimeField(null=True),
        ),
    ]
