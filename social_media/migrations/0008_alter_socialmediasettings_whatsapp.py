# Generated by Django 4.0.2 on 2022-05-02 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_media', '0007_sitesettings_show_title_in_menu_bar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmediasettings',
            name='whatsapp',
            field=models.CharField(blank=True, default='Enter your number', help_text='Whatsapp Number', max_length=100, null=True),
        ),
    ]
