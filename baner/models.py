from django.db import models


class Banner(models.Model):
    title = models.CharField(max_length=250, verbose_name="عنوان بنر")
    link = models.CharField(max_length=250, verbose_name="url بنر")
    image = models.ImageField(upload_to='media/', verbose_name="عکس بنر")
    img_title = models.CharField(max_length=250, verbose_name="عنوان عکس بنر", null=True, blank=True)
    img_alt = models.CharField(max_length=250, verbose_name="متن جایگزین عکس بنر", null=True, blank=True)
    btn_text = models.CharField(max_length=250, verbose_name="متن دکمه بنر", null=True, blank=True)
    class_css = models.CharField(max_length=250, verbose_name="کلاس css", null=True, blank=True)
    style = models.CharField(max_length=500, verbose_name="استایل بنر", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "بنر"
        verbose_name_plural = "بنر ها"
