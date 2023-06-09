from django.db import models

class Pessoa(models.Model):
    class Meta:
        abstract = True
    
    estadoCivilChoices = (
        ('S','Solteiro(a)'),
        ('C','Casado(a)'),
        ('D','Divorciado(a)'),
        ('V','Viúvo(a)'),
        ('O','Outro'),
    )


    nomeCompleto = models.CharField(max_length=50, verbose_name='nome completo')
    email = models.EmailField(max_length=50, verbose_name='email')
    dataNascimento = models.DateField(verbose_name='data nascimento')
    telefone = models.CharField(max_length=12, verbose_name='telefone')
    cpf = models.CharField(max_length=11, unique=True, verbose_name='cpf')
    endereco = models.CharField(max_length=100, verbose_name='endereco')
    estadoCivil = models.CharField(max_length=1, choices=estadoCivilChoices)

    def __str__(self) -> str:
        return self.nomeCompleto
