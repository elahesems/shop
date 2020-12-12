# Generated by Django 3.1.4 on 2020-12-11 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0027_aboutus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name_plural': 'AboutUs'},
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='text',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='detail',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='paragraph1',
            field=models.TextField(blank=True, null=True),
        ),
    ]