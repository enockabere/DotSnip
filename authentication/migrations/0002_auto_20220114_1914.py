# Generated by Django 3.2.8 on 2022-01-14 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(max_length=60, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='profession',
            field=models.CharField(max_length=200, unique=True, verbose_name='Profession'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(max_length=200, verbose_name='Username'),
        ),
    ]