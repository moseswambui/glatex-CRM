# Generated by Django 3.2.5 on 2021-08-22 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managementportal', '0002_dailysales_sales_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailysalesdigital',
            name='Amount_Per_Product',
            field=models.CharField(blank=True, max_length=34, null=True),
        ),
    ]