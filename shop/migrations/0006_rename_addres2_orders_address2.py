# Generated by Django 3.2.25 on 2025-06-27 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_orders_addres2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='addres2',
            new_name='address2',
        ),
    ]
