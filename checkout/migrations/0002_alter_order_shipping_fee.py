# Generated by Django 4.0 on 2022-01-15 18:55

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_fee',
            field=models.DecimalField(decimal_places=2, default=Decimal('15.75'), max_digits=6),
        ),
    ]
