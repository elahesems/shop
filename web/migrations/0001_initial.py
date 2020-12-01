# Generated by Django 3.1.3 on 2020-11-30 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sliders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(blank=True, max_length=100, null=True, verbose_name='en ust sırada yazılacak')),
                ('title2', models.CharField(blank=True, max_length=100, null=True, verbose_name='ortada yazılacak')),
                ('title3', models.CharField(blank=True, max_length=100, null=True, verbose_name='en alt')),
                ('link', models.URLField(blank=True, null=True, verbose_name='website')),
            ],
        ),
    ]