# Generated by Django 3.2.4 on 2021-07-23 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210721_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectstatus',
            name='complete',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=100),
        ),
    ]