# Generated by Django 3.0.8 on 2020-07-08 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='summary',
            field=models.TextField(default='quick summary'),
        ),
    ]