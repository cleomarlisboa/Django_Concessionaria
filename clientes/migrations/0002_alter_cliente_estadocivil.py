# Generated by Django 4.1.7 on 2023-06-21 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='estadoCivil',
            field=models.CharField(choices=[('S', 'Solteiro(a)'), ('C', 'Casado(a)'), ('D', 'Divorciado(a)'), ('V', 'Viúvo(a)'), ('O', 'Outro')], max_length=1),
        ),
    ]