# Generated by Django 3.1.4 on 2020-12-11 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0028_auto_20201211_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team_member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('manager', models.CharField(max_length=100)),
                ('detail', models.CharField(max_length=400)),
                ('img', models.ImageField(upload_to='', verbose_name='resim')),
                ('facebook', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('vimeo', models.URLField(blank=True, null=True)),
                ('tumblr', models.URLField(blank=True, null=True)),
                ('pinterest', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'TeamMember',
            },
        ),
    ]