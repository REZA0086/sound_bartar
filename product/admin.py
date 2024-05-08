from django.contrib import admin
from django.db.models.aggregates import Count
from .models import (Product, Brand, Feature, ProductFeature,
                     ProductGallery, ProductGroup)


# region Brand
def active_brand(modeladmin, request, queryset):
    res = queryset.update(is_active=True)
    message = f'تعداد {res} برند  فعال شد'
    modeladmin.message_user(request, message)


def de_active_brand(modeladmin, request, queryset):
    res = queryset.update(is_active=True)
    message = f'تعداد {res}برند  غیرفعال شد'
    modeladmin.message_user(request, message)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'brand_title', 'register_date')

    actions = [active_brand, de_active_brand]

    active_brand.short_description = 'فعال سازی برندهای انتخابی'
    de_active_brand.short_description = 'غیرفعال کردن برندهای انتخابی'


# endregion

# region Product Group
def active_product_group(modeladmin, request, queryset):
    res = queryset.update(is_active=True)
    message = f'تعداد {res} گروه محصول  فعال شد'
    modeladmin.message_user(request, message)


def de_active_product_group(modeladmin, request, queryset):
    res = queryset.update(is_active=True)
    message = f'تعداد {res}گروه محصول  غیرفعال شد'
    modeladmin.message_user(request, message)


class FeatureInstanceAdminInline(admin.TabularInline):
    model = Feature


# endregion

# region Group Feature

def active_feature(modeladmin, request, queryset):
    res = queryset.update(is_active=True)
    message = f'تعداد {res}ویژگی گروه  فعال شد'
    modeladmin.message_user(request, message)


def de_active_feature(modeladmin, request, queryset):
    res = queryset.update(is_active=True)
    message = f'تعداد {res}ویژگی گروه  غیرفعال شد'
    modeladmin.message_user(request, message)


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title',)

    actions = [active_feature, de_active_feature]

    de_active_feature.short_description = 'غیرفعال سازی ویژگی های انتخابی'
    active_feature.short_description = 'فعال سازی ویژگی های انتخابی'


# endregion

# region Product
def de_active_product(modeladmin, request, queryset):  # برای اضافه کردن اکشن
    res = queryset.update(is_active=False)
    message = f'تعداد {res} کالا غیر فعال شد '
    modeladmin.message_user(request, message)


def active_product(modeladmin, request, queryset):
    res = queryset.update(is_active=True)
    message = f'تعداد {res} کالا  فعال شد '
    modeladmin.message_user(request, message)


class ProductFeatureInstanceAdminInline(admin.TabularInline):
    model = ProductFeature


class ProductGalleryStackedInline(admin.StackedInline):
    model = ProductGallery


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_name', 'id', 'product_discount', 'product_after_discount',
        'product_sell_count',
        'register_date',)


    de_active_product.short_description = 'غیرفعال سازی کالا های انتخابی'
    active_product.short_description = 'فعال سازی کالا های انتخابی'


# endregion

# region Product Tag


# endregion

# region Product Feature
def active_product_feature(modeladmin, request, queryset):
    res = queryset.update(is_active=True)
    message = f'تعداد {res} ویژگی محصول  فعال شد'
    modeladmin.message_user(request, message)


def de_active_product_feature(modeladmin, request, queryset):
    res = queryset.update(is_active=True)
    message = f'تعداد {res}ویژگی محصول  غیرفعال شد'
    modeladmin.message_user(request, message)


@admin.register(ProductFeature)
class ProductFeatureAdmin(admin.ModelAdmin):
    list_display = ('product', 'feature', 'feature_value',)

    actions = [de_active_product_feature, active_product_feature]

    active_product_feature.short_description = 'فعال سازی ویژگی های محصول انتخابی'
    de_active_product_feature.short_description = 'غیرفعال کردن ویژگی های محصول انتخابی'


# endregion

# region Product Gallery
def de_active_product_gallery(modeladmin, request, queryset):  # برای اضافه کردن اکشن
    res = queryset.update(is_active=False)
    message = f'تعداد {res} عکس از گالری غیر فعال شد '
    modeladmin.message_user(request, message)


def active_product_gallery(modeladmin, request, queryset):
    res = queryset.update(is_active=True)
    message = f'تعداد {res} عکس از گالری  فعال شد '
    modeladmin.message_user(request, message)


@admin.register(ProductGallery)
class ProductGalleryAdmin(admin.ModelAdmin):
    list_display = ('product', 'product_picture', 'product_picture_alt', 'product_picture_title')
    actions = [de_active_product_gallery, active_product_gallery]

    active_product_gallery.short_description = 'فعال سازی عکس از گالری محصول انتخابی'
    de_active_product_gallery.short_description = 'غیرفعال کردن عکس از گالری محصول انتخابی'


# endregion

@admin.register(ProductGroup)
class ProductGroupAdmin(admin.ModelAdmin):
    list_display = ('group_title',)
