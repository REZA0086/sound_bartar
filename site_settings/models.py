from django.db import models


class SiteSettings(models.Model):
    title = models.CharField(max_length=250, verbose_name='عنوان سایت')
    logo = models.ImageField(upload_to='media/', verbose_name='لوگوی سایت')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات سایت'


class Seo(models.Model):
    meta_name = models.CharField(max_length=250, verbose_name='نام متا')
    meta_content = models.CharField(max_length=250, verbose_name='مقدار متا')

    site = models.ForeignKey(SiteSettings, on_delete=models.CASCADE, verbose_name='سایت')

    class Meta:
        verbose_name = 'سیُو'
        verbose_name_plural = 'سیُو'


class SocialMedia(models.Model):
    name = models.CharField(max_length=250, verbose_name='نام شبکه')
    url = models.CharField(max_length=250, verbose_name='url شبکه')
    logo = models.ImageField(upload_to='media/', verbose_name='لوگوی شبکه')

    class Meta:
        verbose_name = 'شبکه های اجتماعی'
        verbose_name_plural = 'شبکه های اجتماعی'
