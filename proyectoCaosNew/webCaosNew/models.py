from django.db import models
from django.contrib.auth.models import User
# tablas para pagina del admin.
class Categoria(models.Model):
    categoria=models.CharField(primary_key=True,max_length=60)

    def str(self) -> str:
        return self.categoria




class Noticia(models.Model):
    idnoticia=models.IntegerField(primary_key=True)
    nombre_periodista=models.CharField(max_length=60)
    titulo_noticia=models.CharField(max_length=300,default='--')
    titular_noticia=models.CharField(max_length=300,default='--')
    cuerpo_noticia=models.CharField(max_length=300,default='--')
    foto=models.ImageField(upload_to='fotos',null=True,default='fotos/defaut.png')
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    publicar=models.BooleanField(default=False)
    comentario=models.CharField(max_length=45,default='S/C')
    usuario=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    precio=models.IntegerField(default=100)

    def str(self) -> str:
        return self.nombre_periodista


class Galeria(models.Model):
    idGaleria= models.AutoField(primary_key=True)
    foto = models.ImageField(upload_to='fotos')
    noticia = models.ForeignKey(Noticia,on_delete=models.CASCADE)

    def str(self) -> str:
        return "N°"+str(self.idGaleria)+" /  "+self.noticia.nombre_periodista


class Contacto(models.Model):
    nombre = models.CharField(max_length=45)
    correo = models.CharField(max_length=45)
    fono = models.IntegerField()
    mensaje = models.CharField(max_length=45)

    def str(self):
        return self.nombre

class objcarrito(models.Model):
    idobjeto = models.AutoField(primary_key=True)
    nombre_objeto = models.CharField(max_length=60)
    precio = models.IntegerField()
    foto = models.ImageField(upload_to='fotos',null=True,default='fotos/default.png')