# Generated by Django 3.2.5 on 2022-09-22 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0004_auto_20220922_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]