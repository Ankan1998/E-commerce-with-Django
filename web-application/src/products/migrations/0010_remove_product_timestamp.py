# Generated by Django 4.2.4 on 2023-08-07 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_product_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='timestamp',
        ),
    ]
