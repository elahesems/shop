# Generated by Django 3.1.4 on 2020-12-08 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0023_remove_seyirci_konum'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='markname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='markpic',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='logo mark'),
        ),
    ]