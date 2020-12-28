# Generated by Django 3.1.4 on 2020-12-28 07:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drawlottoapp', '0004_lottonumber_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='lottonumber',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lottonumber',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
