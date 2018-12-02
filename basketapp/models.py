from django.db import models
from geekshop import settings
from mainapp.models import Product

class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    add_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return f'{self.user} -> {self.product}({self.quntity})'
        return '{} -> {}({})'.format(self.user, self.product, self.quantity)

