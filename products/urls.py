from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('product_form/', views.product_form, name='product_form'),
    path('edit_product/<str:pk>', views.edit_product, name='edit_product'),
    path(
        'delete_product/<str:pk>', views.delete_product, name='delete_product'
        ),
]
