from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=60)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        """
        Ensure correct plural of Category
        in admin UI
        """
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
        on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    ingredients = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
