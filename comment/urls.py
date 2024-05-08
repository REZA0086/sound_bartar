from django.urls import path

from comment import views

app_name = 'comment'

urlpatterns = [
    path('comment/', views.comment, name='comment'),
    path('comment_product/<int:product_id>/', views.product_comment, name='product_comment')

]
