# Generated by Django 4.0.2 on 2022-05-14 20:36

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_menuitem_link_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='menu_items',
            field=wagtail.core.fields.StreamField([('Sub_Links', wagtail.core.blocks.StructBlock([('sub_links', wagtail.core.blocks.StreamBlock([('page_link', wagtail.core.blocks.StructBlock([('display_text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock())])), ('external_link', wagtail.core.blocks.StructBlock([('display_text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link', wagtail.core.blocks.CharBlock(label='URL', required=False))]))], label='Sub-links', required=False))]))], blank=True, verbose_name='Dropdown'),
        ),
    ]
