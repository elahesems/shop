# Generated by Django 3.1.4 on 2020-12-07 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_auto_20201206_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, help_text='konum ekleyin:2131/5 sokak no:6 Adalet mahallesi bayraklı', max_length=5000, null=True)),
                ('phone', models.IntegerField(verbose_name='Phone number')),
                ('fax', models.IntegerField(verbose_name='FAX')),
                ('email1', models.EmailField(max_length=254, verbose_name='Email 1')),
                ('email2', models.EmailField(max_length=254, verbose_name='Email 2')),
            ],
        ),
        migrations.RemoveField(
            model_name='footer',
            name='massage',
        ),
        migrations.AlterField(
            model_name='footer',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True, verbose_name='EPOSTA'),
        ),
    ]
