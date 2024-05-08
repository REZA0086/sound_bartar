from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('whishlist/<int:product_id>/', views.whishlist, name='whishlist')
]