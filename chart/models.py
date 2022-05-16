from django.db import models

# Create your models here.
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect


from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from core import blocks
from wagtail.core.blocks import (
    CharBlock, ChoiceBlock, RichTextBlock, StreamBlock, StructBlock, TextBlock,
)
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.table_block.blocks import TableBlock


class BitcoinChart(models.Model):
    name = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(
        verbose_name='slug',
        allow_unicode=True,
        max_length=255,
        null=True,
        )
    date = models.DateTimeField('Date', db_index=True, blank=True)
    value = models.DecimalField('value', max_digits=15, decimal_places=2, default=0)
    

    panels = [
        MultiFieldPanel([
            FieldPanel('name'),
            FieldPanel('slug'),
            ],),
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('value'),
        ])
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Bitcoin'
        ordering = ['date']


class DataIndex(Page):
    subpage_types = [
        'chart.DataPage',
    ]
    pass
    

class DataPage(Page):
    template = 'data_page.html'
    subpage_types = [
        'chart.DataPage',
    ]
    parent_page_types = [
        'chart.DataIndex',
    ]
    
    date = models.DateTimeField(default=timezone.now, verbose_name='Date')
    content = StreamField(
        [
            ('full_richtext', blocks.RichtextBlock()),
            ('simple_richtext', blocks.SimpleRichtextBlock()),
            ('table', TableBlock()),
        ],
        null=True,
        blank=True,
    )
    subtitle = models.CharField(max_length=100, null=True, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('subtitle'),
        StreamFieldPanel('content'),
        ImageChooserPanel('image'),
    ]

    class Meta:
        verbose_name = 'Data'
        verbose_name_plural = 'Data'

