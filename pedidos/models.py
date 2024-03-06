from django.db import models
from site_principal.models import Usuario
# Create your models here.
class Categorias(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome
    

class Lanches(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    valor = models.FloatField()
    categoria = models.ForeignKey(Categorias, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome
    
class ImageBurguer(models.Model):
    foto = models.ImageField(upload_to='foto_burguer')
    lanche = models.ForeignKey(Lanches, on_delete=models.DO_NOTHING)




class Sobremesa(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    quantidade = models.IntegerField()
    valor = models.FloatField()
    imagem = models.ImageField(upload_to='img_complemento_pedido')

class Bebidas(models.Model):
    nome = models.CharField(max_length=50)
    quantidade = models.IntegerField()
    valor = models.FloatField()
    imagem = models.ImageField(upload_to='img_complemento_pedido')

class Acompanhamento(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    quantidade = models.IntegerField()
    valor = models.FloatField()
    imagem = models.ImageField(upload_to='img_complemento_pedido')

class Extra(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    quantidade = models.IntegerField()
    valor = models.FloatField()
    imagem = models.ImageField(upload_to='img_complemento_pedido')


class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    lanche = models.ForeignKey(Lanches, on_delete=models.DO_NOTHING)
    extra = models.ForeignKey(Extra, on_delete=models.DO_NOTHING, null=True, blank=True)
    acompanhamento = models.ForeignKey(Acompanhamento, on_delete=models.DO_NOTHING, null=True, blank=True)
    sobremesa = models.ForeignKey(Sobremesa, on_delete=models.DO_NOTHING, null=True, blank=True)
    bebida = models.ForeignKey(Bebidas, on_delete=models.DO_NOTHING, null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    quantidade_extra = models.IntegerField(null=True, blank=True, default=0)
    quantidade_acompanhamento = models.IntegerField(null=True, blank=True, default=0)
    quantidade_sobremesa = models.IntegerField(null=True, blank=True, default=0)
    quantidade_bebida = models.IntegerField(null=True, blank=True, default=0)
    finalizado = models.CharField(max_length=3,null=True, blank=True, default='NÃO')
    valor = models.FloatField()


#TODO: Criar função que verifica se tem categorias criadas para poder cadastrar um lanche
