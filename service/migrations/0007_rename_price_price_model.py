# Generated by Django 4.0.5 on 2022-06-30 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0004_add_vehicle'),
        ('service', '0006_rename_regular_service_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='price',
            new_name='price_model',
        ),
    ]