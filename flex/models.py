"""Flexible page for About, Terms of Condition, Privacy Policy Page"""

from django.db import models
from django.shortcuts import render

# Create your models here.

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from core import blocks
from wagtail.core.blocks import (
    CharBlock, ChoiceBlock, RichTextBlock, StreamBlock, StructBlock, TextBlock,
)

from blog.models import BlogPage


class FlexPage(Page):
    template = "flex/flex_page.html"

    content = StreamField(
        [
            ('title_and_text', blocks.TitleAndTextBlock()),
            ('full_richtext', blocks.RichtextBlock()),
            ('simple_richtext', blocks.SimpleRichtextBlock()),
            ('cards', blocks.CardBlock()),
            ('cta', blocks.CTABlock()),
            ('button', blocks.ButtonBlock()),
            ('image', blocks.ImageBlock()),
            ('heading', blocks.HeadingBlock()),
            ('block', blocks.BlockQuote()),
            ('TOC_Article', blocks.TOC()),
            ('char_block', CharBlock(
                required=True,
                help_text='',
                min_length=10,
                max_length=50,
                template='blocks/char_block.html',
                icon = "title",
            ))
        ],
        null=True,
        blank=True,
    )

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name = 'Flex Page'
        verbose_name_plural = 'Flex Pages'


    def get_context(self, request):

        # Filter by tag
        latest = BlogPage.objects.live().public().order_by('-first_published_at')[:5]

        # Update template context
        context = super(FlexPage, self).get_context(request)
        context['latest'] = latest
        return context
