from django.db import models
from django_jalali.db import models as jmodels
import jdatetime
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from account.models import CustomerUser


# region Brand
class Brand(models.Model):
    brand_title = models.CharField(max_length=250, verbose_name='عنوان برند')
    brand_image = models.ImageField(upload_to='media/', verbose_name='لوگو',null=True, blank=True)
    brand_image_alt = models.CharField(max_length=100, null=True, blank=True, verbose_name='متن جایگزین لوگو')
    brand_image_title = models.CharField(max_length=100, null=True, blank=True, verbose_name='عنوان لوگو')
    register_date = jmodels.jDateField(default=jdatetime.date.today(), verbose_name='تاریخ ساخت')

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'

    def __str__(self):
        return self.brand_title


# endregion

# region Product Group
class ProductGroup(models.Model):
    group_title = models.CharField(max_length=100, verbose_name='عنوان گروه کالا')
    group_image = models.ImageField(upload_to='products/groups/', blank=True, null=True,
                                    verbose_name='لوگو دسته بندی')
    group_image_alt = models.CharField(max_length=100, null=True, blank=True, verbose_name='متن جایگزین لوگو')
    group_image_title = models.CharField(max_length=100, null=True, blank=True, verbose_name='عنوان لوگو')

    def __str__(self):
        return self.group_title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


# endregion

# region Group Feature
class Feature(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان ویژگی')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ویژگی گروه محصول'
        verbose_name_plural = 'ویژگی های گروه محصولات'


# endregion

# region Product
class Product(models.Model):
    product_name = models.CharField(max_length=200, verbose_name='نام کالا')
    cover_picture = models.ImageField(upload_to='media/product/', verbose_name='تصویر اصلی کالا')
    group_image_alt = models.CharField(max_length=100, null=True, blank=True, verbose_name='متن جایگزین کاور')
    group_image_title = models.CharField(max_length=100, null=True, blank=True, verbose_name='عنوان کاور')
    price = models.IntegerField(verbose_name='قیمت ', default=0)
    product_discount = models.IntegerField(default=0, verbose_name='تخفیف')
    product_after_discount = models.IntegerField(default=0, null=True, blank=True, verbose_name='قیمت پس از تخفیف')
    exist_count = models.IntegerField(default=0, verbose_name='تعداد محصول')
    product_view_count = models.IntegerField(default=0, verbose_name='تعداد بازدید')
    product_sell_count = models.IntegerField(default=0, verbose_name='تعداد فروش')
    register_date = jmodels.jDateField(default=jdatetime.date.today(), verbose_name='تاریخ درج')
    music = models.FileField(upload_to='media/product/music/', verbose_name='صدای محصول', null=True, blank=True)

    product_group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE,verbose_name='گروه کالا', related_name='products_of_groups')
    brand = models.ForeignKey(Brand, verbose_name='برند کالا', null=True, on_delete=models.CASCADE,
                              related_name='brands')


    def after_discount(self):
        self.product_after_discount = self.price - ((self.price * self.product_discount) / 100)
        return self.product_after_discount

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    # Todo: باید قیمت پس از تخفیف رو توی تابع ذخیره با بازنویسی درست کرد


# region Product Feature
class ProductFeature(models.Model):
    feature_value = models.CharField(max_length=200, verbose_name='مقدار ویژگی')
    product = models.ForeignKey(Product,related_name='feature_product', on_delete=models.CASCADE, verbose_name='محصول')
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, verbose_name='ویژگی')

    def __str__(self):
        return f'{self.product} - {self.feature} : {self.feature_value}'

    class Meta:
        verbose_name = 'ویژگی محصول'
        verbose_name_plural = 'ویژگی های محصولات'


# endregion

# region Product Gallery
class ProductGallery(models.Model):
    product_picture = models.ImageField(upload_to='media/gallery/', verbose_name='تصویر')
    product_picture_alt = models.CharField(max_length=100, null=True, blank=True, verbose_name='متن جایگزین تصویر')
    product_picture_title = models.CharField(max_length=100, null=True, blank=True, verbose_name='عنوان تصویر')

    product = models.ForeignKey(Product, related_name='product_gallery', on_delete=models.CASCADE, verbose_name='کالا')

    class Meta:
        verbose_name = ' گالری محصول'
        verbose_name_plural = 'گالری محصولات'


# endregion

class Rating(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, verbose_name="کاربر امتیاز دهنده")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, verbose_name="امتیاز محصول")
    value = models.PositiveIntegerField(null=True, blank=True, default=0, verbose_name="مقدار امتیاز")

    class Meta:
        verbose_name = "امتیاز محصول"
        verbose_name_plural = "امتیاز محصولات"


class WishList(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, verbose_name="کاربر")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
