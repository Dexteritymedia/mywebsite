# Generated by Django 4.0.2 on 2022-05-24 16:25

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('chart', '0009_datapageblogcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataListingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('heading', wagtail.core.fields.StreamField([('jumbotron', wagtail.core.blocks.StructBlock([('jumbotron', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(max_length=40, required=False)), ('description', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'bold', 'italic', 'link'], required=False)), ('color', wagtail.core.blocks.CharBlock(help_text='Enter a hexdecimal color for the background e.g #000000', max_length=40, required=False)), ('text_color', wagtail.core.blocks.CharBlock(help_text='Enter a hexdecimal color for the text e.g #000000 or red', max_length=40, required=False))])))]))], blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Data Category',
                'verbose_name_plural': 'Data Categories',
            },
            bases=('wagtailcore.page',),
        ),
    ]