# Generated by Django 4.0.2 on 2022-05-09 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_homepage_subtitle_imageshomepage_datahomepage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='header',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
