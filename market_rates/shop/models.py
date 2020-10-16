from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """
    info about category
    """
    name = models.CharField(("categoria"), max_length=50)

    class Meta:
        verbose_name  = "categoria"
        verbose_name_plural  = "categorias"


    def __str__(self):
        return "{}".format(self.name)


class Product(models.Model):
    """
    here info about product information
    """
    name        = models.CharField(("Nombre del producto"), blank=False, max_length=25)
    price       = models.DecimalField(("Precio"), max_digits=4, decimal_places=2)
    image       = models.ImageField(("Imagen"), upload_to=None, height_field=None, width_field=None, max_length=None)
    description = models.TextField(("Descripcion del producto"))
    category    = models.ForeignKey(Category, verbose_name=("Categoria"), on_delete=models.CASCADE)

    def __str__(self):
        return "{} Q.{} => {}".format(self.name, self.price, self.category)

class Quote(models.Model):
    
    product = models.ForeignKey(Product, verbose_name=("Producto"), on_delete=models.CASCADE)
    quanti  = models.IntegerField(("Cantidad"))
    client  = models.ForeignKey(User, verbose_name=("cliente"), on_delete=models.CASCADE)

    def __str__(self):
        return "{} cantidad:{} Cliente que lo solicita {}".format(self.product, self.quanti, self.client)