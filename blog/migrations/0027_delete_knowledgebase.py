# Generated by Django 4.0.2 on 2022-05-02 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_knowledgebase_tags'),
    ]

    operations = [
        migrations.DeleteModel(
            name='KnowledgeBase',
        ),
    ]
