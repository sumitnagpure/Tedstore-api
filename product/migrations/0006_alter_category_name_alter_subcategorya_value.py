# Generated by Django 5.0.1 on 2024-02-19 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='subcategorya',
            name='value',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
