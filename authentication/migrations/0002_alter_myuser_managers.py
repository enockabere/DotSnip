# Generated by Django 3.2.12 on 2022-03-31 14:19

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='myuser',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
