# Generated by Django 3.2.4 on 2021-07-30 19:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210729_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectstatus',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
