# Generated by Django 4.1.7 on 2023-04-22 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0009_alter_versao_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='versao',
            name='imagem',
            field=models.FileField(blank=True, null=True, upload_to='carros'),
        ),
    ]
