# Generated by Django 3.2.4 on 2021-07-15 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_projectstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='project_details',
            field=models.TextField(blank=True, default='Enter Project Details', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='project_title',
            field=models.CharField(default='Enter Project Title', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='projectstatus',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], default='Pending', max_length=50),
        ),
    ]