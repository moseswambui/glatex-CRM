# Generated by Django 3.2.5 on 2021-08-16 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managementportal', '0018_screenprintingexpenses_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailySalesDigital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Client', models.CharField(blank=True, max_length=45, null=True)),
                ('Product_Size', models.CharField(blank=True, max_length=50, null=True)),
                ('Client_id', models.CharField(blank=True, max_length=45, null=True)),
                ('Sales_Product', models.CharField(blank=True, max_length=34, null=True)),
                ('Sales_Quantity', models.CharField(blank=True, max_length=34, null=True)),
                ('Sales_Amount', models.IntegerField(blank=True, null=True)),
                ('Balance', models.IntegerField(blank=True, null=True)),
                ('Sales_Date', models.DateField(blank=True, null=True)),
                ('Payment_Method', models.CharField(blank=True, choices=[('MPESA', 'M-pesa'), ('CASH', 'Cash'), ('CHEQUE', 'Cheque')], max_length=20, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='dailysales',
            name='Category',
        ),
        migrations.AlterField(
            model_name='dailysales',
            name='Product_Size',
            field=models.CharField(blank=True, choices=[('A3', 'A3'), ('A4', 'A4')], max_length=50, null=True),
        ),
    ]