# Generated by Django 5.1.6 on 2025-02-17 12:55

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allowance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('from_date', models.DateTimeField()),
                ('to_date', models.DateTimeField()),
                ('active', models.BooleanField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_allowance', to='shop.product')),
            ],
        ),
    ]
