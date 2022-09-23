from django.db import models

# Create your models here.
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from core import blocks
from wagtail.core.blocks import (
    CharBlock, ChoiceBlock, RichTextBlock, StreamBlock, StructBlock, TextBlock,
)
from wagtail.admin.edit_handlers import (
    FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel )

from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.table_block.blocks import TableBlock

from wagtail.snippets.edit_handlers import SnippetChooserPanel

from wagtailseo.models import SeoMixin, SeoType, TwitterCard

from blog.models import BlogCategory


from wagtail.admin.edit_handlers import TabbedInterface, ObjectList

from core.blocks import VisualBlock

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
    template = 'data_index.html'


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


    class Meta:
        verbose_name = 'Mainpage'
        verbose_name_plural = 'Mainpage'


class DataListingPage(Page):
    template = "data_listing_page.html"

    subpage_types = ['chart.DataPage']
    parent_page_types = [
        'chart.DataIndex'
        ]


    heading = StreamField(
        [
            
            ('jumbotron', blocks.JumbotronBlockWithTextColor()),
        ],
        null=True,
        blank=True,
    )
    

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            StreamFieldPanel('heading'),
            ], heading='Additional Information'),
    ]


    class Meta:
        verbose_name = 'Data Category'
        verbose_name_plural = 'Data Categories'



    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = DataListingPage.get_children(self,).live().order_by('-first_published_at')
        all_posts = DataPage.objects.live().public().order_by('-first_published_at')

        if request.GET.get('tag', None):
            tags = request.GET.get('tag')
            all_posts = all_posts.filter(tags__slug__in=[tags])
        

        paginator = Paginator(blogpages, 20)

        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context['posts'] = posts
        context['categories'] = BlogCategory.objects.all()
        return context




class DataPage(SeoMixin, Page):
    template = 'data_page.html'
    subpage_types = [
        'chart.DataPage',
    ]
    parent_page_types = [
        'chart.DataIndex', 'chart.DataListingPage'
    ]
    
    date = models.DateTimeField(default=timezone.now, verbose_name='Date')
    content = StreamField(
        [
            ('chart', VisualBlock()),
            ('full_richtext', blocks.RichtextBlock()),
            ('simple_richtext', blocks.SimpleRichtextBlock()),
            ('image', blocks.ImageBlock()),
            ('table', TableBlock(template='blocks/table_block.html')),
        ],
        null=True,
        blank=True,
    )
    
    subtitle = models.CharField(max_length=100, null=True, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )

    
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        StreamFieldPanel('content'),
        ImageChooserPanel('image'),
    ]


    sidebar_content_panels = [
        FieldPanel('subtitle'),
        InlinePanel('data_categories', label="category", max_num=1),
    ]
        
    seo_content_type = SeoType.ARTICLE

    seo_twitter_card = TwitterCard.LARGE
    
    promote_panels = SeoMixin.seo_panels


    edit_handler = TabbedInterface([
        
        ObjectList(content_panels, heading='Content', classname='Content',),
        ObjectList(sidebar_content_panels, heading='More Content'),
        #ObjectList(Page.promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings', classname='settings'),
        ObjectList(SeoMixin.seo_panels, heading='SEO', classname='seo'),
    ])
    
    class Meta:
        verbose_name = 'Data post'
        verbose_name_plural = 'Data Posts'


class DataPageBlogCategory(models.Model):
    page = ParentalKey('chart.DataPage', on_delete=models.CASCADE, related_name='data_categories')
    blog_category = models.ForeignKey(
        'blog.BlogCategory', on_delete=models.CASCADE, related_name='data_pages')

    panels = [
        SnippetChooserPanel('blog_category'),
        ]

    class Meta:
        unique_together = ('page', 'blog_category')

