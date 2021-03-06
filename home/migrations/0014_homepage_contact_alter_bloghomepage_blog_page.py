# Generated by Django 4.0.2 on 2022-05-22 19:40

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0035_alter_bloglistingpage_heading'),
        ('home', '0013_alter_homepage_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='contact',
            field=wagtail.core.fields.StreamField([('contact', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=60, required=True)), ('text', wagtail.core.blocks.TextBlock(features=['bold', 'italic'], required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(default='Get in Touch', max_length=40, required=True)), ('select', wagtail.core.blocks.BooleanBlock(blank=True, help_text='Select to use 2 columns', verbose_name='Two Columns'))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bloghomepage',
            name='blog_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='blog.blogpage'),
        ),
    ]
