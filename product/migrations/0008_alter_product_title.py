# Generated by Django 5.0.1 on 2024-02-19 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_subcategoryb_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
