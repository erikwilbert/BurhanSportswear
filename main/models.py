from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=255, null=True, blank=True)
    price=models.IntegerField(null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    thumbnail=models.URLField(blank=True, null=True)
    category=models.CharField(max_length=20, default="none")
    is_featured=models.BooleanField(default=False)
    views=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
    def increment_views(self):
        self.views += 1
        self.save()