# Generated by Django 4.0.5 on 2022-07-12 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0004_add_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brands',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
