# Generated by Django 4.0.4 on 2022-05-15 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['pk'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['category'], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]
