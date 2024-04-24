# Generated by Django 5.0.4 on 2024-04-22 16:47

import django.db.models.deletion
import django_jalali.db.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver_address', models.TextField(verbose_name='آدرس گیرنده')),
                ('received_phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='شماره تماس گیرنده')),
                ('received_full_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='نام گیرنده')),
                ('is_paid', models.BooleanField(verbose_name='نهایی شده / نشده')),
                ('payment_date', django_jalali.db.models.jDateField(auto_now=True, null=True, verbose_name='تاریخ پرداخت')),
                ('tracking_code', models.CharField(blank=True, max_length=11, null=True, verbose_name='کد پیگیری')),
                ('status', models.CharField(choices=[('Collecting', 'Collecting'), ('Collected', 'Collected'), ('Delivered', 'Delivered'), ('Returned', 'Returned')], default='Collecting', max_length=10, verbose_name='وضیعت')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نام مشتری')),
            ],
            options={
                'verbose_name': 'سبد خرید',
                'verbose_name_plural': 'سبدهای خرید کاربران',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final_price', models.IntegerField(blank=True, null=True, verbose_name='قیمت نهایی تکی محصول')),
                ('count', models.IntegerField(verbose_name='تعداد')),
                ('order', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='invoice.order', verbose_name='سبد خرید')),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='محصول سبد خرید')),
            ],
            options={
                'verbose_name': 'جزییات سبد خرید',
                'verbose_name_plural': 'لیست جزییات سبدهای خرید',
            },
        ),
    ]
