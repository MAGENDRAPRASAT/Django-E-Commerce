# Generated by Django 5.0.1 on 2024-01-05 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='category',
            new_name='categoryId',
        ),
    ]
