# Generated by Django 3.0.8 on 2021-03-30 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_api', '0004_auto_20210330_0531'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['name'], 'verbose_name': 'Client', 'verbose_name_plural': 'Clients'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='store',
            options={'ordering': ['name'], 'verbose_name': 'Store', 'verbose_name_plural': 'Stores'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='store',
        ),
        migrations.AddField(
            model_name='product',
            name='store_id',
            field=models.ManyToManyField(to='tienda_api.Store'),
        ),
    ]
