# Generated by Django 5.1.6 on 2025-03-22 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_orders_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='email',
            field=models.CharField(error_messages={'unique': 'A user with that contact already exists.'}, max_length=100, unique=True),
        ),
    ]
