# Generated by Django 4.2.6 on 2023-10-29 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow_flow', '0002_alter_borrowedbook_borrow_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrowedbook',
            old_name='terms_accepted',
            new_name='terms_accepted_1',
        ),
        migrations.AddField(
            model_name='borrowedbook',
            name='terms_accepted_2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='borrowedbook',
            name='terms_accepted_3',
            field=models.BooleanField(default=False),
        ),
    ]
