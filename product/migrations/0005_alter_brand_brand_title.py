# Generated by Django 5.0.4 on 2024-04-23 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_brand_brand_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_title',
            field=models.CharField(max_length=250, unique=True, verbose_name='عنوان برند'),
        ),
    ]
