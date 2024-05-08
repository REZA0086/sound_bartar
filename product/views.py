from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View
from product.models import *
from comment.models import ProductComment
from product.models import ProductFeature,ProductGallery


class ProductDetailView(View):
    def get(self, request, product_id):
        if product_id:
            product = Product.objects.get(id=product_id)
            comments = ProductComment.objects.filter(product_id=product_id)
            product_feature = ProductFeature.objects.filter(product_id=product_id)
            product_gallery = ProductGallery.objects.filter(product_id=product_id)

            # Todo return render(request, 'page/product/product_detail.html',context={'product':product,'comments':comments})
            return redirect('main:index')
        else:
            messages.error(request, 'صفحه مورد نظر یافت نشد')
            return redirect('main:index')  # Todo صفحه 404
