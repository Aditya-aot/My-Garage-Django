# Generated by Django 4.0.5 on 2022-06-30 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_alter_price_model_package_alter_price_model_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.service'),
        ),
    ]
