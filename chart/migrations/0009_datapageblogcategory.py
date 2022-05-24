# Generated by Django 4.0.2 on 2022-05-22 19:55

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0035_alter_bloglistingpage_heading'),
        ('chart', '0008_alter_datapage_content_alter_datapage_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataPageBlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data_pages', to='blog.blogcategory')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='data_categories', to='chart.datapage')),
            ],
            options={
                'unique_together': {('page', 'blog_category')},
            },
        ),
    ]