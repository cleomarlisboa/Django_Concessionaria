# Generated by Django 4.1.7 on 2023-04-22 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0011_alter_versao_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='versao',
            name='ano',
            field=models.IntegerField(default=2023),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='versao',
            name='modelo',
            field=models.IntegerField(default=2023),
            preserve_default=False,
        ),
    ]
