# Generated by Django 5.1.1 on 2024-09-16 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_prodectmodel_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodectmodel',
            name='in_stock',
            field=models.BooleanField(default=True),
        ),
    ]
