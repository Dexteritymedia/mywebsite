# Generated by Django 4.0.2 on 2022-05-02 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_media', '0008_alter_socialmediasettings_whatsapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmediasettings',
            name='whatsapp',
            field=models.CharField(blank=True, default='Enter your WhatsApp number', help_text='Whatsapp Number', max_length=100, null=True),
        ),
    ]
