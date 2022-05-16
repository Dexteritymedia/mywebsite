# Generated by Django 4.0.2 on 2022-05-14 20:37

import core.blocks
from django.db import migrations, models
import django.db.models.deletion
import wagtail.contrib.table_block.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailcore', '0066_collection_management_permissions'),
        ('chart', '0005_delete_dataindex_delete_datapage'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataIndex',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='DataPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('date', models.DateTimeField(blank=True, db_index=True, verbose_name='Date')),
                ('content', wagtail.core.fields.StreamField([('full_richtext', core.blocks.RichtextBlock()), ('simple_richtext', core.blocks.SimpleRichtextBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock())], blank=True, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'Data',
                'verbose_name_plural': 'Data',
            },
            bases=('wagtailcore.page',),
        ),
    ]