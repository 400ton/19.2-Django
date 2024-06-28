# Generated by Django 4.2 on 2024-06-24 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_product_is_published_product_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('cancellation_of_publication', 'Canceling the publication of the product'), ('changes_the_description', 'Changes the description of any product'), ('changes_the_category', 'Changes the category of any product')], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]