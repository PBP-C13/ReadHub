# Generated by Django 4.2.6 on 2023-10-28 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorit', '0003_favorit_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorit',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]