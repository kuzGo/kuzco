""" Favourite items list model"""

from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Favourites(models.Model):
    """ Favourite items list model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    watches = models.ManyToManyField(
        Product, through="AddFavourites", related_name='favourites')

    def __str__(self):
        return str(self.user)


class AddFavourites(models.Model):
    """ Adding items to Favourite list"""
    watch = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    favourites = models.ForeignKey(
        Favourites, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.watch.name)
