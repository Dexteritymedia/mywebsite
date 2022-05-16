# Generated by Django 4.0.2 on 2022-05-15 14:24

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_menuitem_menu_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='menu_items',
            field=wagtail.core.fields.StreamField([('Sub_Links', wagtail.core.blocks.StructBlock([('display_text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('sub_links', wagtail.core.blocks.StreamBlock([('page_link', wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock())])), ('external_link', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Title', max_length=200, required=True)), ('link', wagtail.core.blocks.CharBlock(label='URL', required=False))]))], label='Sub-links', required=False))]))], blank=True, verbose_name='Dropdown'),
        ),
    ]
