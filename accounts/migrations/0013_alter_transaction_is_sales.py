# Generated by Django 5.0.4 on 2024-06-04 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_remove_trade_bill_number_remove_trade_discount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='is_sales',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]