# Generated by Django 4.0.5 on 2022-07-14 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_remove_paymentdetails_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentdetails',
            name='payment_id',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='paymentdetails',
            name='transaction_id',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
