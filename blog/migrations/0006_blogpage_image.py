# Generated by Django 4.0.2 on 2022-03-19 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('blog', '0005_blogtagindexpage_blogcategory_blogpage_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
