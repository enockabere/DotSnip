# Generated by Django 3.2.12 on 2022-03-26 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20220326_1238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='price',
            new_name='total',
        ),
        migrations.AddField(
            model_name='cart',
            name='unit_price',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
