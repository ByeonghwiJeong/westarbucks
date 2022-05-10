from django.db import models

class Menu(models.Model):
  name = models.CharField(max_length=50)
  class Meta:
    db_table = 'menus'

class Category(models.Model):
  name = models.CharField(max_length=20)
  menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
  class Meta:
    db_table = 'categories'

class Nutrition(models.Model):
  sodium_mg = models.DecimalField(max_digits=6, decimal_places=2)
  protein_g = models.DecimalField(max_digits=6, decimal_places=2)
  size_ml = models.DecimalField(max_digits=6, decimal_places=2)
  class Meta:
    db_table = 'nutritions'

class Allergy(models.Model):
  name = models.CharField(max_length=100)
  class Meta:
    db_table = 'allergies'

class ProductAllergy(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete = models.CASCADE)
    product = models.ForeignKey('Product', on_delete = models.CASCADE)
    class Meta:
        db_table = 'products_allergies'

class Product(models.Model):
    korean_name  = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)
    description  = models.TextField()
    category     = models.ForeignKey('Category', on_delete=models.CASCADE)
    nutrition    = models.OneToOneField('Nutrition', on_delete=models.CASCADE)
    allergies    = models.ManyToManyField('Allergy', through = 'ProductAllergy')
    class Meta:
        db_table = 'products'

class Image(models.Model):
    image_url = models.CharField(max_length=100)
    product   = models.ForeignKey('Product', on_delete=models.CASCADE)
    class Meta:
        db_table = 'images'