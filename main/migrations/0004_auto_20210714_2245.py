# Generated by Django 3.2.4 on 2021-07-14 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210714_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_title',
            name='user',
        ),
        migrations.DeleteModel(
            name='Project_Status',
        ),
        migrations.DeleteModel(
            name='Project_Title',
        ),
    ]
