# Generated by Django 3.1.7 on 2021-04-17 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insightly', '0024_auto_20210417_1159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category1041trust',
            old_name='category1041Trust_id',
            new_name='category1041trust_id',
        ),
        migrations.RenameField(
            model_name='project1041trust',
            old_name='project1041Trust_id',
            new_name='project1041trust_id',
        ),
        migrations.RenameField(
            model_name='project1065x',
            old_name='project1065X_id',
            new_name='project1065x_id',
        ),
        migrations.RenameField(
            model_name='stage1041trust',
            old_name='stage1041Trust_id',
            new_name='stage1041trust_id',
        ),
        migrations.RenameField(
            model_name='usermodel1041trust',
            old_name='usermodel1041Trust_id',
            new_name='usermodel1041trust_id',
        ),
        migrations.RenameField(
            model_name='usermodel1065x',
            old_name='usermodel1065X_id',
            new_name='usermodel1065x_id',
        ),
    ]
