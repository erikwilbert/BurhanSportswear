from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=255, null=True, blank=True)
    price=models.IntegerField(null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    thumbnail=models.URLField(blank=True, null=True)
    category=models.CharField(max_length=20, default="none")
    is_featured=models.BooleanField(default=False)

    def __str__(self):
        return self.name