
from ast import mod
from tkinter.font import names
from urllib import request
from xml.parsers.expat import model
from django.shortcuts import get_object_or_404, render, redirect
from . import models
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import Payment



# Create your views here.
def main (request):
    all_sales=models.sales.objects.all()
    sales_dict={"sales":all_sales}
    return render(request, "sales_app/main.html", context=sales_dict)


def info (request):
    return render(request, "sales_app/info.html")


@login_required(login_url="/login")
def sales_product(request):
    if request.POST:
        name=request.POST["name"]
        price=request.POST["price"]
        image=request.POST["image"]
        models.sales.objects.create(name=name, price=price, image=image)
        return redirect(reverse("main"))
    else:
        return render(request, "sales_app/add_product.html")
    
    
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"


@login_required
def sales(request):
    if request.POST:
        name = request.POST.get("name")
        card_number = request.POST.get("card_number")
        expiration_date = request.POST.get("expiration_date")
        cvv = request.POST.get("cvv")
        models.Payment.objects.create(name=name, card_number=card_number, expiration_date=expiration_date, cvv=cvv)
        return redirect(reverse("success_pay"))
    else:
        return render(request, "sales_app/sale.html")
@login_required      
def success_pay(request):
    return render(request, "sales_app/success.html")


@login_required # type: ignore

def delete_price(request, id):
    sale=models.sales.objects.get(pk=id)
    if request.user== sale.name:
        models.sales.objects.filter(id==id).delete()
        return redirect ('main')
    
    
def view_cart(request):
    cart = models.Cart.objects.get_or_create(user=request.user)[0]
    cart_items = models.CartItem.objects.filter(cart=cart)

    # Hesaplama view'da yapılıyor
    total_price = 0
    for item in cart_items:
        total_price += item.product.price * item.quantity

    return render(request, 'sales_app/view_cart.html', {'cart': cart, 'cart_items': cart_items, 'total_price': total_price})