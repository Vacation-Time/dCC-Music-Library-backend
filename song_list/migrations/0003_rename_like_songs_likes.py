# Generated by Django 4.0.3 on 2022-03-11 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('song_list', '0002_songs_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='songs',
            old_name='like',
            new_name='likes',
        ),
    ]