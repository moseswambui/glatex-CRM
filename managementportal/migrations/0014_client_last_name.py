# Generated by Django 3.2.5 on 2021-07-31 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managementportal', '0013_alter_glatexemployee_employee_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='Last_Name',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]
