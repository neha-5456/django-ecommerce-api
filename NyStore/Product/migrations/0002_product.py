# Generated by Django 5.1.6 on 2025-03-05 05:10

import Product.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField(blank=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, upload_to=Product.models.product_image_path)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=models.SET(Product.models.get_default_product_category), related_name='product_list', to='Product.productcategory')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
