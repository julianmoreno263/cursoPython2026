
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    image=models.ImageField(verbose_name='Imagen')
    title=models.CharField(max_length=100,verbose_name='Título')
    desc=models.TextField(verbose_name='Descripción')
    content=RichTextField(verbose_name='Contenido')
    created=models.DateTimeField(auto_now_add=True,verbose_name='Fecha Creación')
    update=models.DateTimeField(auto_now=True,verbose_name='Fecha Actualización')

    class Meta:
        verbose_name='Publicación'
        verbose_name_plural='Publicaciones'
        ordering=['-created']


    def __str__(self):
        return self.title