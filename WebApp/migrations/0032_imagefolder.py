# Generated by Django 4.2.4 on 2023-09-22 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0031_image_foldername'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageFolder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
