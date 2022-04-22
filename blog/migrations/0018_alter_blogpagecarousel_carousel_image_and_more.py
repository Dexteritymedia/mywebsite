# Generated by Django 4.0.2 on 2022-04-20 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('wagtailimages', '0023_add_choose_permissions'),
        ('blog', '0017_blogcategory_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpagecarousel',
            name='carousel_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AlterField(
            model_name='blogpagecarousel',
            name='carousel_page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.page'),
        ),
    ]
