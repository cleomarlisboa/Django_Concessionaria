# Generated by Django 4.1.7 on 2023-04-22 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0002_remove_compra_carro_compra_versao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='fornecedor',
        ),
    ]
