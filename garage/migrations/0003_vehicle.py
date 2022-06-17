# Generated by Django 4.0.5 on 2022-06-16 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0002_rename_product_brands'),
    ]

    operations = [
        migrations.CreateModel(
            name='vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='garage.brands')),
            ],
        ),
    ]