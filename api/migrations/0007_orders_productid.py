# Generated by Django 5.1.6 on 2025-03-22 22:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='productid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='api.products'),
        ),
    ]
