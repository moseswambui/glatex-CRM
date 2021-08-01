# Generated by Django 3.2.5 on 2021-07-30 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managementportal', '0002_remove_glatexmeeting_meeting_venue'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlatexContractors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone_Number', models.CharField(blank=True, max_length=16, null=True)),
                ('Contractor_Responsibilities', models.CharField(blank=True, choices=[('LARGEFORMAT', 'Large Format'), ('Electricity', 'Electrician')], max_length=30, null=True)),
                ('Contractor_bio', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
    ]
