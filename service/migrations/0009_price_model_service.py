# Generated by Django 4.0.5 on 2022-06-30 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_remove_price_model_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='price_model',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.service'),
        ),
    ]