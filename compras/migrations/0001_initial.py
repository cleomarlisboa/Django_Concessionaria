# Generated by Django 4.2.2 on 2023-06-24 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataHora', models.DateTimeField()),
                ('quantidade', models.IntegerField()),
                ('valorTotal', models.FloatField()),
                ('versao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='carros.versao')),
            ],
            options={
                'permissions': (('permissao_gerente', 'permissao gerente'), ('permissao_supervisor', 'permissao supervisor'), ('permissao_vendedor', 'permissao vendedor'), ('permissao_funcionario', 'permissao todos funcionarios')),
            },
        ),
    ]
