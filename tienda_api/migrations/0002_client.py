# Generated by Django 3.0.8 on 2021-03-23 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('identification', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]