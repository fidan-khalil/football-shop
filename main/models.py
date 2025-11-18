import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    CATEGORY_CHOICES = [
        ('sepatu', 'Sepatu'),
        ('jersey', 'Jersey'),
        ('bola', 'Bola'),
        ('sarung tangan', 'Sarung Tangan'),
        ('aksesoris', 'Aksesoris'),
    ]

    BRAND_CHOICES = [
        ('nike', 'Nike'),
        ('adidas', 'Adidas'),
        ('puma', 'Puma'),
        ('new balance', 'New Balance'),
        ('under armour', 'Under Armour'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    category = models.CharField(choices=CATEGORY_CHOICES, default='sepatu')
    brand = models.CharField(choices=BRAND_CHOICES, default='nike')
    thumbnail = models.URLField()
    price = models.IntegerField()
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=0.0,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(5.0)
        ]
    )
    description = models.TextField()
    
    def __str__(self):
        return self.name