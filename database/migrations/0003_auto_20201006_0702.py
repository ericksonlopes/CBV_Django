# Generated by Django 2.2.9 on 2020-10-06 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Article',
        ),
    ]