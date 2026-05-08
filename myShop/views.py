from django.shortcuts import render

from .models import Category, Product


def categories(request):
    categories_list = Category.objects.all()
    return render(request, 'myShop/categories.html', {'categories': categories_list})


def products(request):
    products_list = Product.objects.all()
    return render(request, 'myShop/products.html', {'products': products_list})


def category_products(request, category_id):
    category = Category.objects.get(id=category_id)
    products_list = Product.objects.filter(category=category)
    return render(
        request,
        'myShop/category_products.html',
        {'category': category, 'products': products_list},
    )
