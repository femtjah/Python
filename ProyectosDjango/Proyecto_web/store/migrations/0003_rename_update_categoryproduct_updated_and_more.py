# Generated by Django 4.0 on 2021-12-30 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_created_product_update'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoryproduct',
            old_name='update',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='update',
            new_name='updated',
        ),
    ]
