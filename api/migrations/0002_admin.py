# Generated by Django 5.1.6 on 2025-03-05 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'admin',
            },
        ),
    ]
