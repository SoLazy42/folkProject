# Generated by Django 5.0.4 on 2024-04-19 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folk', '0007_rename_imageholder_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='Image',
            field=models.ImageField(upload_to='config/static/images'),
        ),
    ]
