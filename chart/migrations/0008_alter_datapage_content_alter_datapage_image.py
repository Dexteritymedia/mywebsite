# Generated by Django 4.0.2 on 2022-05-22 19:40

import core.blocks
from django.db import migrations, models
import django.db.models.deletion
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('chart', '0007_alter_datapage_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapage',
            name='content',
            field=wagtail.core.fields.StreamField([('full_richtext', core.blocks.RichtextBlock()), ('simple_richtext', core.blocks.SimpleRichtextBlock()), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('shadow', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Add Shadow'), ('S', 'Small Shadow'), ('R', 'Regular Shadow'), ('L', 'Larger Shadow')], required=False))])), ('table', wagtail.contrib.table_block.blocks.TableBlock())], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='datapage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]