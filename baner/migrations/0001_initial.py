# Generated by Django 5.0.4 on 2024-05-07 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='عنوان بنر')),
                ('link', models.CharField(max_length=250, verbose_name='url بنر')),
                ('image', models.ImageField(upload_to='media/', verbose_name='عکس بنر')),
                ('img_title', models.CharField(blank=True, max_length=250, null=True, verbose_name='عنوان عکس بنر')),
                ('img_alt', models.CharField(blank=True, max_length=250, null=True, verbose_name='متن جایگزین عکس بنر')),
                ('btn_text', models.CharField(blank=True, max_length=250, null=True, verbose_name='متن دکمه بنر')),
                ('class_css', models.CharField(blank=True, max_length=250, null=True, verbose_name='کلاس css')),
                ('style', models.CharField(blank=True, max_length=500, null=True, verbose_name='استایل بنر')),
            ],
            options={
                'verbose_name': 'بنر',
                'verbose_name_plural': 'بنر ها',
            },
        ),
    ]
