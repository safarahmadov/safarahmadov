from os import name
from django import views
from django.contrib import admin
from django.urls import path
from . import views

from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.main, name="main"),
    path("sales/", views.sales, name="sales"), # type: ignore
    path("info/", views.info, name="info"),
    path("sales_product/", views.sales_product, name="sales_product"),
    path('signup/',views.SignUpView.as_view(),name="signup"),
    path("success_pay/", views.success_pay, name="success_pay"),
    path('delete_price/<int:id>', views.delete_price , name='delete_price'),  # type: ignore
    path('cart/', views.view_cart, name='view_cart'),]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)