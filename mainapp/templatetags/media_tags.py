from django import template
from django.conf import settings

register = template.Library()

@register.filter(name='media_product')
def media_product(path):
    if not path:
        path = 'products_images/default.jpg'
    return f'{settings.MEDIA_URL}{path}'

# register.filter('media_product', media_product)