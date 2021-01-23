# Generated by Django 3.1.4 on 2020-12-15 11:01

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0035_auto_20201215_1035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='colorField',
        ),
        migrations.AddField(
            model_name='product',
            name='colorField1',
            field=colorfield.fields.ColorField(blank=True, default=None, max_length=18, null=True, verbose_name='1.renk'),
        ),
        migrations.AddField(
            model_name='product',
            name='colorField2',
            field=colorfield.fields.ColorField(blank=True, default=None, max_length=18, null=True, verbose_name='2.renk'),
        ),
        migrations.AddField(
            model_name='product',
            name='colorField3',
            field=colorfield.fields.ColorField(blank=True, default=None, max_length=18, null=True, verbose_name='3.renk'),
        ),
        migrations.AddField(
            model_name='product',
            name='colorField4',
            field=colorfield.fields.ColorField(blank=True, default=None, max_length=18, null=True, verbose_name='4.renk'),
        ),
    ]
