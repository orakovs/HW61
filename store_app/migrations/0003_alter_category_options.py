# Generated by Django 4.2.3 on 2023-07-25 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0002_category_good'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]