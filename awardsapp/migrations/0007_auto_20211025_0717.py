# Generated by Django 3.2.8 on 2021-10-25 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awardsapp', '0006_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='average_rate',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
