# Generated by Django 3.1.4 on 2020-12-13 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0002_auto_20201213_1254'),
        ('articleapp', '0002_auto_20201213_0604'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='article', to='projectapp.project'),
        ),
    ]
