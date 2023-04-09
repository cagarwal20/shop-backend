from django.db import models

# Create your models here.
CATEGORY_CHOICES = [
    ('Accessories', 'Accessories'),
    ('Kurtis', 'Kurtis'),
    ('Leggings', 'Leggings'),
    ('Pants', 'Pants'),
]
class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    ratings = models.SmallIntegerField()
    image = models.CharField(max_length=200,default="")
    mrp=models.FloatField(default=0)
    disc=models.IntegerField(default=0)
    sale_price=models.FloatField(default=0)
    category = models.CharField(max_length=20,choices=CATEGORY_CHOICES,default="Kurtis")
    
    def __str__(self):
        return self.name

