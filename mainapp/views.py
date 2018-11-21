from django.shortcuts import render
import json

def main(request):
    # title = 'Главная'
    # products = [
    #         {
    #             "name": "Отличный стул",
    #             "desc": "Расположитесь комфортно",
    #             "image_src": "product-1.jpg",
    #             "image_href": "/product/1/",
    #             "alt": "продукт 1"
    #         },
    #         {
    #             "name": "Стул повышенного качества",
    #             "desc": "Не оторваться",
    #             "image_src": "product-2.jpg",
    #             "image_href": "/product/2/",
    #             "alt": "продукт 2"
    #         }
    # ]
    # content = {'title': title, 'products': products}
    json_data = open('static/products.json').read()
    content = json.loads(json_data)
    return render(request, 'mainapp/index.html', content)


def products(request):
    title = 'Продукты'
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    same_products = [
        {
            'name': 'Отличный стул',
            'desc': 'Не оторваться',
            'image_src': 'product-11.jpg',
            'alt': 'продукт 11'
        },
        {
            'name': 'Стул повышенного качества',
            'desc': 'Комфортно',
            'image_src': 'product-21.jpg',
            'alt': 'продукт 21'
        },
        {
            'name': 'Стул премиального качества',
            'desc': 'Просто попробуйте',
            'image_src': 'product-31.jpg',
            'alt': 'продукт 31'
        }
    ]
    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html')
