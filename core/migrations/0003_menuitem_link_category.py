# Generated by Django 4.0.2 on 2022-04-18 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_blogcategory_description'),
        ('core', '0002_footertext_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='link_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='blog.blogcategory'),
        ),
    ]