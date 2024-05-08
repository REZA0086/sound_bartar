from django.db import models
from product.models import Product
from account.models import CustomerUser
from django_jalali.db import models as jmodels
import jdatetime
from django.utils.html import mark_safe

from uuid import uuid4
from django.utils.crypto import get_random_string


class Order(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, blank=True, null=True, verbose_name="نام مشتری")
    receiver_address = models.TextField(verbose_name='آدرس گیرنده')
    received_phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='شماره تماس گیرنده')
    received_full_name = models.CharField(max_length=150, blank=True, null=True, verbose_name='نام گیرنده')
    is_paid = models.BooleanField(verbose_name="نهایی شده / نشده")
    payment_date = jmodels.jDateField(auto_now=True, verbose_name="تاریخ پرداخت", blank=True, null=True)
    tracking_code = models.CharField(max_length=11, blank=True, null=True, verbose_name="کد پیگیری")
    status = (
        ('Collecting', 'Collecting'), ('Collected', 'Collected'), ('Delivered', 'Delivered'), ('Returned', 'Returned'))
    status = models.CharField(max_length=10, choices=status, default='Collecting', verbose_name="وضیعت")

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "سبد خرید"
        verbose_name_plural = "سبدهای خرید کاربران"

    def calculate_total_price(self):
        total = 0

        for order_detail in self.orderdetail_set.all():
            total += order_detail.product.after_discount()

        return int(total)

    def calculate_total(self):
        total_amount = 0

        for order_detail in self.orderdetail_set.all():
            if self.is_paid:
                total_amount += order_detail.final_price
            else:
                total_amount += order_detail.product.after_discount() * order_detail.count

        return int(total_amount)


class OrderDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, verbose_name="محصول سبد خرید")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, verbose_name="سبد خرید")
    final_price = models.IntegerField(verbose_name="قیمت نهایی تکی محصول", blank=True, null=True)
    count = models.IntegerField(verbose_name="تعداد")

    class Meta:
        verbose_name = "جزییات سبد خرید"
        verbose_name_plural = "لیست جزییات سبدهای خرید"

    def __str__(self):
        return str(self.order)

    def get_final_price(self):
        return self.product.after_discount() * self.count

    def Final_Price(self):
        return self.get_final_price()
