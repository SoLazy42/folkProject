# Generated by Django 5.0.4 on 2024-04-19 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('folk', '0009_alter_image_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='Image',
            new_name='image',
        ),
    ]
