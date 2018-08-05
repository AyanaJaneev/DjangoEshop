from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Category, Product
from cart.cart import Cart
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    cart_product_form = CartAddProductForm()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/list.html', context)

@require_POST
def product_add(request, product_id):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.remove(product=product)
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'cart_product_form': form
    }
    return render(request, 'shop/product/list.html', context)
