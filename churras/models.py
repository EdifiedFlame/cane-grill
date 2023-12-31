from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from pessoas.models import Pessoa
# Create your models here.
# Esta classe de models se tornara uma tabela no banco de dados
class Prato(models.Model):
    #serão os campos da tabela (atributos da classe)
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_prato = models.CharField(
        max_length=100,
        verbose_name='Nome do Prato',
        )
    ingredientes = models.TextField(
        verbose_name='ingredientes',
    )
    modo_preparo = models.TextField(
        verbose_name='Modo de Preparo',
    )
    tempo_preparo = models.PositiveBigIntegerField(
        verbose_name='Tempo de Preparo',
    )
    rendimento = models.CharField(max_length=100,
        verbose_name='Rendimento'
    )
    categoria = models.CharField(max_length=100,
        verbose_name='Categoria',
    )
    date_prato = models.DateField(
        default=datetime.now, blank=True
    )
    foto_prato = models.ImageField(
        upload_to= 'pratos/%Y/%m',
        blank=True
    )
    publicado = models.BooleanField(default=False)
   
    def __str__(self):
       return self.nome_prato
   
    class Meta:
       verbose_name='Prato'
       verbose_name_plural = 'Pratos'