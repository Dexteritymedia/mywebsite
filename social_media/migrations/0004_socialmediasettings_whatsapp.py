# Generated by Django 4.0.2 on 2022-04-26 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_media', '0003_sitesettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmediasettings',
            name='whatsapp',
            field=models.URLField(blank=True, default='Enter your number', help_text='Whatsapp Number', max_length=100, null=True),
        ),
    ]
