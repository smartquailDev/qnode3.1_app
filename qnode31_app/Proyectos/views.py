from django.shortcuts import render, get_object_or_404
from .models import mantenimiento, Project
from cart.forms import CartAddProductForm

def product_list(request, category_slug=None):
    category = None
    user=None
    categories = mantenimiento.objects.all()
    products =  Project.objects.filter(available=True)
    productos =  Project.objects.filter(user=user)
    if category_slug:
        categories = get_object_or_404(mantenimiento, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 
        'proyectos/list.html',  
        {'category':category,
        'categories':categories,
        'products':products,
        'productos':productos})

def product_detail(request,id,slug):
    product = get_object_or_404(Project,id=id,slug=slug,available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
    'proyectos/detail.html',
    {'product':product,
    'cart_product_form' : cart_product_form}
    )
