from django.db import models


class Slider(models.Model):
    title = models.CharField(max_length=250, verbose_name="عنوان اسلایدر")
    link = models.CharField(max_length=250, verbose_name="url اسلایدر")
    image = models.ImageField(upload_to='media/', verbose_name="عکس اسلایدر")
    img_title = models.CharField(max_length=250, verbose_name="عنوان عکس اسلایدر", null=True, blank=True)
    img_alt = models.CharField(max_length=250, verbose_name="متن جایگزین عکس اسلایدر", null=True, blank=True)
    btn_text = models.CharField(max_length=250, verbose_name="متن دکمه اسلایدر", null=True, blank=True)
    class_css = models.CharField(max_length=250, verbose_name="کلاس css", null=True, blank=True)
    style = models.CharField(max_length=500, verbose_name="استایل اسلایدر", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "اسلایدر"
        verbose_name_plural = "اسلایدر ها"
