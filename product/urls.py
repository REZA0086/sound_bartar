from django.urls import path
from product import views

app_name = 'product'
urlpatterns = [
    path('product/<int:product_id>', views.ProductDetailView.as_view(), name='product-detail')
]