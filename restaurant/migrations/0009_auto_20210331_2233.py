# Generated by Django 3.1.2 on 2021-03-31 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_auto_20210330_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemsize',
            name='item_size',
            field=models.CharField(default='', max_length=15),
        ),
    ]