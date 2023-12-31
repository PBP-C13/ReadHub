# Generated by Django 4.2.6 on 2023-10-23 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_book_authors_alter_book_book_desc_and_more'),
        ('discussion_forum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forum',
            old_name='pesan',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='forum',
            name='gambar',
        ),
        migrations.AddField(
            model_name='forum',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='book.book'),
            preserve_default=False,
        ),
    ]
