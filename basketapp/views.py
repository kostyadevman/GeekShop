from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from mainapp.models import Product
from basketapp.models import Basket

def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)

    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket()
        basket.product = product
        basket.user = request.user

    basket.quantity += 1
    basket.save()

    return redirect(request.META['HTTP_REFERER'])
