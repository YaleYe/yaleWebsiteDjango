# Generated by Django 3.0.8 on 2020-08-18 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('phone', models.IntegerField(max_length=15)),
            ],
        ),
    ]
