# Generated by Django 5.0.4 on 2024-04-18 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='category',
            field=models.CharField(default='Теоритическая часть', max_length=150),
        ),
    ]
