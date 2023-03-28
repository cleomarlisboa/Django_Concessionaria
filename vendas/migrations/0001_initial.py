# Generated by Django 4.1.7 on 2023-03-28 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('colaboradores', '0003_alter_colaborador_situacaovinculo'),
        ('carros', '0002_rename_placa_carro_placacarro'),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataHora', models.DateTimeField()),
                ('detalhes', models.CharField(max_length=50)),
                ('valorVenda', models.DecimalField(decimal_places=2, max_digits=15)),
                ('formaPagamento', models.CharField(max_length=20)),
                ('carro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='carros.carro')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientes.cliente')),
                ('colaborador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='colaboradores.colaborador')),
            ],
        ),
    ]
