from django.shortcuts import render, get_object_or_404
import datetime
from .models import ProductCategory, Product
from basketapp.models import Basket
import random, os, json


JSON_PATH = 'mainapp/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)




        
def main(request):
    title = 'главная'  
    products = Product.objects.all()[:3]
    
    content = {
        'title': title,
        'products': products,
        'basket': get_basket(request.user),
    }
    
    return render(request, 'mainapp/index.html', content)
    

def products(request, pk=None):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    basket = get_basket(request.user)
           
    if pk:
        if pk is None:
            category = {'name': 'все'}
            products = Product.objects.all().order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')
        
        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'basket': basket,
        }
        
        return render(request, 'mainapp/products_list.html', content)
    
    same_products = get_same_products(hot_product)
    
    content = {
        'title': title,
        'links_menu': links_menu, 
        'same_products': same_products,
        'basket': basket,
    }
    
    return render(request, 'mainapp/products.html', content)
    

def contact(request):
    title = 'о нас'
    visit_date = datetime.datetime.now()
    
    locations = load_from_json('contact__locations')
    
    content = {
        'title': title,
        'visit_date':visit_date, 
        'locations': locations,
        'basket': get_basket(request.user),
    }
    
    return render(request, 'mainapp/contact.html', content)
    
    
