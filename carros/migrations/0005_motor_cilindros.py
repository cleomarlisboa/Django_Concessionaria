# Generated by Django 4.1.7 on 2023-04-17 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0004_alter_versao_acessorios'),
    ]

    operations = [
        migrations.AddField(
            model_name='motor',
            name='cilindros',
            field=models.IntegerField(default=3),
        ),
    ]
