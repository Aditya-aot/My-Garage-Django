# Generated by Django 4.0.5 on 2022-06-16 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='brands',
        ),
    ]