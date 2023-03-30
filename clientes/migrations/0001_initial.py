# Generated by Django 4.1.7 on 2023-03-30 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCompleto', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('dataNascimento', models.DateField()),
                ('telefone', models.CharField(max_length=12)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('endereco', models.CharField(max_length=100)),
                ('estadoCivil', models.CharField(max_length=20)),
                ('renda', models.DecimalField(decimal_places=2, max_digits=15)),
                ('profissao', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]