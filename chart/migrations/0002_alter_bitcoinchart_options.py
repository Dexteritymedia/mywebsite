# Generated by Django 4.0.2 on 2022-05-08 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bitcoinchart',
            options={'ordering': ['date'], 'verbose_name_plural': 'Bitcoin'},
        ),
    ]