from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE,
                                 null=True, blank=True)
    watches = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    title = models.CharField(max_length=255)
    review = models.TextField()

    def __str__(self):
        return self.title
