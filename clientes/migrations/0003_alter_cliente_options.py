# Generated by Django 4.2.2 on 2023-06-24 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_alter_cliente_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'permissions': (('permissao_gerente', 'permissao gerente'), ('permissao_supervisor', 'permissao supervisor'), ('permissao_vendedor', 'permissao vendedor'), ('permissao_funcionario', 'permissao todos funcionarios'))},
        ),
    ]
