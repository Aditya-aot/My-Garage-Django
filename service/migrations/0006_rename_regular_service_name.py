# Generated by Django 4.0.5 on 2022-06-30 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_rename_service_test_price_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='Regular',
            new_name='name',
        ),
    ]
