# Generated by Django 4.1.4 on 2022-12-23 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blogcommentary_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
