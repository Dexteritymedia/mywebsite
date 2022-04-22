# Generated by Django 4.0.2 on 2022-03-08 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_media', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmediasettings',
            name='facebook',
            field=models.URLField(blank=True, default='www.facebook.com/', help_text='Facebook URL', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='socialmediasettings',
            name='instagram',
            field=models.URLField(blank=True, default='www.instagram.com/', help_text='Instagram URL', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='socialmediasettings',
            name='linkedin',
            field=models.URLField(blank=True, default='www.linkedin.com/', help_text='Linkedin URL', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='socialmediasettings',
            name='pinterest',
            field=models.URLField(blank=True, default='www.pinterest.com/', help_text='Pinterest URL', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='socialmediasettings',
            name='twitter',
            field=models.URLField(blank=True, default='www.twitter.com/', help_text='Twitter URL', max_length=100, null=True),
        ),
    ]
