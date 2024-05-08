from django.conf import settings
from django.shortcuts import render
from django.views.generic import View
from baner.models import Banner
from blog.models import BlogCategory, Blog, BlogTag
from invoice.models import Order, OrderDetail
from product.models import Product, Brand, ProductGroup, Feature, Rating, WishList
from site_settings.models import SocialMedia, Seo, SiteSettings
from slider.models import Slider


def media_url(request):
    return {'media_url': settings.MEDIA_URL}


class IndexView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        banners = Banner.objects.all()
        products = Product.objects.all()
        blogs = Blog.objects.all()
        site_settings = SiteSettings.objects.all()
        sliders = Slider.objects.all()
        category = ProductGroup.objects.all()
        brand = Brand.objects.all()
        seo = Seo.objects.all()
        social_media = SocialMedia.objects.all()

        new_products = Product.objects.all().order_by('register_date')
        sell_products = Product.objects.all().order_by('product_sell_count')


        context = {
            'media_url': settings.MEDIA_URL,
            'user': user,
            'banners': banners,
            'products': products,
            'blogs': blogs,
            'site_settings': site_settings,
            'sliders': sliders,
            'category': category,
            'brand': brand,
            'social_media': social_media,
            'seo': seo,
            'new_products': new_products,
            'sell_products': sell_products,

        }
        return render(request, 'page/main/index.html', context)


def whishlist(request, product_id):
    whish = WishList.objects.create(product_id=product_id, user=request.user)
    return whish
