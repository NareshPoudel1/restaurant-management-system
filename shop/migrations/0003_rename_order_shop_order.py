# Generated by Django 4.1.6 on 2023-05-13 09:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0002_remove_order_status_order_order_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='shop_order',
        ),
    ]