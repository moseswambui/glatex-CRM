# Generated by Django 3.2.5 on 2021-08-22 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managementportal', '0004_auto_20210822_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailysales',
            name='Product_Size',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]