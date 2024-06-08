# Generated by Django 5.0.4 on 2024-05-28 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_trade_tradeitem_delete_transactionitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='bill_number',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trade',
            name='discount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trade',
            name='is_sales',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]