# Generated by Django 4.0.2 on 2022-05-03 06:23

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('blog', '0031_delete_blogcategoryindexpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='KnowledgeBaseIndex',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.core.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'KnowledgeBase',
                'verbose_name_plural': 'KnowledgeBase',
            },
            bases=('wagtailcore.page',),
        ),
    ]