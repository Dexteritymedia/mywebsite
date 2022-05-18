from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey

from core import blocks
from blog.models import BlogPage
from chart.models import DataPage


class ImagesHomePage(Orderable):

    page = ParentalKey('home.HomePage', related_name='moving_images', blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    

    panels = [

        ImageChooserPanel('image'),
    ]


class DataHomePage(Orderable):

    page = ParentalKey('home.HomePage', related_name='data_pages', blank=True)
    data_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.CASCADE,
        )
    

    panels = [

        PageChooserPanel('data_page', ['chart.DataPage','blog.BlogPage']),
    ]


class BlogHomePage(Orderable):

    page = ParentalKey('home.HomePage', related_name='blog_pages', blank=True)
    blog_page = models.ForeignKey(
        'blog.BlogPage',
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.CASCADE,
        )
    

    panels = [

        PageChooserPanel('blog_page'),
    ]



class HomePage(Page):
    max_count = 1
    
    image_heading = models.CharField(max_length=250, null=True, blank=True, verbose_name='heading')
    blog_heading = models.CharField(max_length=250, null=True, blank=True, verbose_name='heading')
    data_heading = models.CharField(max_length=250, null=True, blank=True, verbose_name='heading')
    content = StreamField(
        [
            
            ('jumbotron', blocks.JumbotronBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
        MultiFieldPanel(
            [FieldPanel('data_heading',),
             InlinePanel('data_pages', max_num=5, min_num=0, label='Data Page',),
             ],
            heading='Data Visual',
            classname='collapsible collapsed',
            ),
        MultiFieldPanel(
            [FieldPanel('blog_heading',),
             InlinePanel('blog_pages', max_num=5, min_num=0, label='Blog Page',),
             ],
            heading='Blog Pages',
            classname='collapsible collapsed',
            ),
        MultiFieldPanel(
            [FieldPanel('image_heading',),
             InlinePanel('moving_images', max_num=7, min_num=5, label='Image',),
             ],
            heading='Images',
            classname='collapsible collapsed',
            ),
    ]
    
