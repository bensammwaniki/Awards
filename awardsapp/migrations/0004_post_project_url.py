# Generated by Django 3.2.8 on 2021-10-24 23:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('awardsapp', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='project_url',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
