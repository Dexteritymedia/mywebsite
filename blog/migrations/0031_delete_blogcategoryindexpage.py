# Generated by Django 4.0.2 on 2022-05-02 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_alter_blogpagecarousel_carousel_page'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogCategoryIndexPage',
        ),
    ]
