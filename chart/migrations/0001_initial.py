# Generated by Django 4.0.2 on 2022-05-06 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BitcoinChart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('slug', models.SlugField(allow_unicode=True, max_length=255, null=True, verbose_name='slug')),
                ('date', models.DateTimeField(blank=True, db_index=True, verbose_name='Date')),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='value')),
            ],
            options={
                'verbose_name_plural': 'Bitcoin',
                'ordering': ['name'],
            },
        ),
    ]
