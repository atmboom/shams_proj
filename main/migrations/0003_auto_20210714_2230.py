# Generated by Django 3.2.4 on 2021-07-14 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210714_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='project_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='project_title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
