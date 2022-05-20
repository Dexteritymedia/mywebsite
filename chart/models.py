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
    max_count = 1
    template = 'data.html'
    subpage_types = [
        'chart.DataPage',
    ]


    def get_context(self, request):
        context = super().get_context(request)
        all_posts = DataPage.objects.live().public().order_by('-first_published_at')


        if request.GET.get('tag', None):
            tags = request.GET.get('tag')
            all_posts = all_posts.filter(tags__slug__in=[tags])
        

        paginator = Paginator(all_posts, 20)

        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context['posts'] = posts
        return context
    

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
            ('image', blocks.ImageBlock()),
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

