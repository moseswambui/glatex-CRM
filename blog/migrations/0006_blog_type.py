# Generated by Django 4.1.4 on 2022-12-15 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20221204_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.type'),
        ),
    ]
