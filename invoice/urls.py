from django.urls import path
from invoice import views

app_name = "order"

urlpatterns = [
    path('orders/', views.add_product_to_order, name='add_orders'),
    path('remove_order/', views.remove_from_cart, name='remove_order'),
    path('add_order/', views.add_from_cart, name='add_from_cart'),
]