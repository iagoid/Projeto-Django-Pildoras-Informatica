# Generated by Django 3.0.7 on 2020-08-18 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='imagem',
            field=models.ImageField(upload_to='servicios', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='Atualizado em'),
        ),
    ]
