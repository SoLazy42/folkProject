# Generated by Django 5.0.4 on 2024-04-19 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folk', '0004_parsing_useful'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('Image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
