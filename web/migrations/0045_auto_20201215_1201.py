# Generated by Django 3.1.4 on 2020-12-15 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0044_auto_20201215_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('tl', 'TL'), ('usd', 'USD'), ('euro', 'EURO')], default='tl', max_length=5, verbose_name='kur'),
        ),
    ]
