# Generated by Django 3.1.4 on 2020-12-28 08:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drawlottoapp', '0009_auto_20201228_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lottonumber',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lotto', to=settings.AUTH_USER_MODEL),
        ),
    ]
