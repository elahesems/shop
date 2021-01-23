# Generated by Django 3.1.4 on 2020-12-15 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0040_auto_20201215_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('₺', 'TL'), ('$', 'USD'), ('e€uro', 'EURO')], default='tl', max_length=5, verbose_name='kur'),
        ),
    ]