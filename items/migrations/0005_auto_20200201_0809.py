# Generated by Django 2.1.5 on 2020-02-01 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
