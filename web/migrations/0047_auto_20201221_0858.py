# Generated by Django 3.1.4 on 2020-12-21 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0046_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('tl', '₺'), ('usd', '$'), ('euro', '€')], default='tl', max_length=5, verbose_name='kur'),
        ),
    ]
