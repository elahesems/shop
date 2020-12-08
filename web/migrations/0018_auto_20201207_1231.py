# Generated by Django 3.1.4 on 2020-12-07 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_auto_20201207_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seyirci',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(help_text=':2131/5 sokak no:6 Adalet mahallesi bayraklı', max_length=500)),
                ('phone', models.IntegerField(max_length=100, verbose_name='phonenumber')),
                ('fax', models.IntegerField(max_length=100, verbose_name='fax')),
                ('email1', models.EmailField(max_length=100)),
                ('email2', models.EmailField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'contacts',
            },
        ),
        migrations.DeleteModel(
            name='Contacts',
        ),
    ]