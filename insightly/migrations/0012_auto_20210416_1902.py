# Generated by Django 3.1.7 on 2021-04-16 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insightly', '0011_auto_20210416_1855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stage1120x',
            old_name='stage1120X_id',
            new_name='stage1120x_id',
        ),
        migrations.RenameField(
            model_name='usermodel1120x',
            old_name='usermodel1120X_id',
            new_name='usermodel1120x_id',
        ),
    ]
