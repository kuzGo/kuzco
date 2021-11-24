"""
Update order total on lineitem
update/create and on lineitem delete
"""
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def order_total_update(sender, instance, created, **kwargs):
    instance.order.total_update()


@receiver(post_delete, sender=OrderLineItem)
def order_total_delete(sender, instance, **kwargs):
    instance.order.total_update()
