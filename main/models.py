from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    description=models.TextField()
    thumbnail=models.URLField(blank=True, null=True)
    category=models.CharField(max_length=20, default="none")
    is_featured=models.BooleanField(default=False)
    views=models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    def increment_views(self):
        self.views += 1
        self.save()