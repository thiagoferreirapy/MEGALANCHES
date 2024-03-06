from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=60)
    cpf = models.CharField(max_length=12)  
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)




    def __str__(self) -> str:
        return self.nome
    
class ImgUsuario(models.Model):
    img = models.ImageField(upload_to='fotos_perfil', null=True, blank=True)
    img_user = models.ForeignKey(Usuario, on_delete = models.DO_NOTHING)
    

    def __str__(self) -> str:
        return self.img_user