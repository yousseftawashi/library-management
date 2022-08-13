from django.db import models

# Create your models here.

class category(models.Model):
    name_category = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name_category

class book(models.Model):

    status_book = [
        ('Available','Available'),
        ('rental','rental'),
        ('sold','sold'),
    ]

    name_book = models.CharField(max_length=25)
    author = models.CharField(max_length=50, null=True, blank=True)
    potho_book = models.ImageField(upload_to ='photos')
    potho_author = models.ImageField(upload_to ='photos')
    pages = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True )
    rentel_price_day = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True )
    rental_period = models.IntegerField(null=True, blank=True )
    total_rental = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True )
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=status_book, null=True, blank=True)
    category =models.ForeignKey(category, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return self.name_book

   

