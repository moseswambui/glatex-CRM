from django.urls import path
from . import views

urlpatterns = [
    path("",views.Index, name="homeindex"),
    path("shop",views.Shop, name="shop"),
    path("services/",views.Services, name="services"),
    path("services/category/<slug:servicecategory_slug>",views.Services, name="service_by_category"),
    path("cart",views.Cart, name="cart"),
    path("add_cart/<int:product_id>/",views.add_cart, name="add_cart"),
    path("remove_cart/<int:product_id>/",views.remove_cart, name="remove_cart"),

    path("shop/category/<slug:category_slug>/",views.Shop, name="product_by_category"),
    path("shop/category/<slug:producttype_slug>/",views.Shop, name="product_by_type"),
    path("shop/category/<slug:producttag_slug>/",views.Shop, name="product_by_tag"),

    path("shop/category/<slug:category_slug>/<slug:product_slug>",views.ProductDetail, name="product_detail"),
    path("about",views.AboutUs, name="aboutus"),
    path("checkout",views.Checkout, name="checkout"),
    path("contacts",views.ContactUs, name="contactus"),
    path("shop/search/",views.search, name="search"),
]
