""" Review Model """

from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):
    """ Review's Model """
    username = models.ForeignKey(
        User, related_name="reviews", on_delete=models.CASCADE,
        null=True, blank=True)
    watches = models.ForeignKey(
        Product, related_name="reviews", on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    title = models.CharField(max_length=255)
    review = models.TextField(max_length=500)

    def __str__(self):
        return str(self.title)
