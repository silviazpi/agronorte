from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100, default='')
    descripcion = models.CharField(max_length=500, default='', verbose_name='descripción')
    marca = models.CharField(
        choices=[('Akpil', 'Akpil'),
                 ('BTI', 'BTI'),
                 ('Jeantil', 'Jeantil')],
        default='Akpil',
        max_length=10,
    )
    categoria = models.CharField(
        choices=[('Labor de suelo', 'Labor de suelo'),
                 ('Siembra', 'Siembra'),
                 ('Transporte', 'Transporte'),
                 ('Equipos para la ganadería', 'Equipos para la ganadería'),
                 ('Accesorios', 'Accesorios')],
        default='Labor de suelo',
        max_length=15, verbose_name='categoría'
    )
    subcategoria = models.CharField(
        choices=[('Gradas rápidas', 'Gradas rápidas'),
                 ('Gradas lentas', 'Gradas lentas'),
                 ('Arados', 'Arados')],
        max_length=15, verbose_name='subcategoría', blank=True
    )
    foto1 = models.ImageField(upload_to='productos', default='')
    foto2 = models.ImageField(upload_to='productos', default='')
    foto3 = models.ImageField(upload_to='productos', default='')
    documentacion = models.FileField(default='', verbose_name='documentación', blank=True)
    slug = models.SlugField(unique=True, default='')

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return "/productos/%s/" % self.slug


class Chollo(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    foto = models.ImageField(upload_to='productos', default='')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return "/ocasion/%s/" % self.slug


class Documento(models.Model):
    titulo = models.CharField(max_length=100, default='')
    descripcion = models.CharField(max_length=500, default='', verbose_name='descripción')
    archivo = models.FileField(default='', verbose_name='documentación', blank=True)
    slug = models.SlugField(unique=True, default='')

    def __str__(self):
        return self.titulo

class Noticia(models.Model):
    titulo= models.CharField(default='', max_length=50)
    fecha = models.DateField(default='')
    contenido = models.CharField(default='', max_length=100)
    foto = models.ImageField(default='')

    def __str__(self):
        return self.titulo