# Generated by Django 3.2.5 on 2021-08-05 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managementportal', '0008_dailyexpenses_employee_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dailyexpenses',
            old_name='Expense_Nature',
            new_name='Item_Name',
        ),
    ]