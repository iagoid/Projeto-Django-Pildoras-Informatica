# Generated by Django 3.0.7 on 2020-09-13 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200913_1900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categoria',
            new_name='categorias',
        ),
    ]
