# Generated by Django 2.2.1 on 2019-06-03 19:40

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('tache', '0002_auto_20190603_1939'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ListList',
            new_name='BoardList',
        ),
    ]