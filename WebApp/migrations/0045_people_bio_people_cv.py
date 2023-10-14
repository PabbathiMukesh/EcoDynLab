# Generated by Django 4.1 on 2023-10-13 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0044_title_people_people'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='bio',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='people',
            name='cv',
            field=models.FileField(default='', null=True, upload_to='cv_files/'),
        ),
    ]