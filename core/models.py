from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.core.models import Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel



class MenuItem(Orderable):

    link_title = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        )
    link_url = models.CharField(
        max_length=500,
        blank=True,
        )
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.CASCADE,
        )
    link_category = models.ForeignKey(
        'blog.BlogCategory',
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.CASCADE,
        )
    open_in_new_tab = models.BooleanField(default=False, blank=True)

    page = ParentalKey('Menu', related_name='menu_items')


    panels = [
        FieldPanel('link_title'),
        FieldPanel('link_url'),
        PageChooserPanel('link_page'),
        SnippetChooserPanel('link_category'),
        FieldPanel('open_in_new_tab'),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        if self.link_category:
            return self.link_category.slug
        return '#'

    @property
    def title(self):
        if self.link_page and not self.link_title:
            return self.link_page.title
        elif self.link_title:
            return self.link_title
        elif self.link_category and not self.link_title:
            return self.link_category
        return 'Missing Title'




    """This is for the Validation"""
    
    def clean(self, *args, **kwargs):
        if not self.link_page and not self.link_category and not self.link_url:
            msg = _('Please choose an internal page or custom URL or choose a category')
            raise ValidationError({'link_page': msg})
        if self.link_url and self.link_page and self.link_category:
            msg = _('Linking to a page, a category and custom URL is not permitted')
            raise ValidationError({'link_page': msg, 'link_url':msg, 'link_category':msg})
        if self.link_url and self.link_page:
            msg = _('Linking to a page and custom URL is not permitted')
            raise ValidationError({'link_page': msg, 'link_url':msg})
        if self.link_url and self.link_category:
            msg = _('Linking to a category and custom URL is not permitted')
            raise ValidationError({'link_url':msg, 'link_category':msg})
        if self.link_page and self.link_category:
            msg = _('Linking to a page, and a category is not permitted')
            raise ValidationError({'link_page': msg, 'link_category':msg})
        if self.link_url and not self.link_title:
            msg = _('This field is required when linking to a custom URL')
            raise ValidationError({'link_title': msg})
        super().clean(*args, **kwargs)

"""
    def clean(self):
        if self.link_page is not None and self.link_category is not None:
            raise ValidationError('Select either the link page or the link category')
        if self.link_url is not None and self.link_page is not None:
            raise ValidationError('Select one of either link url or link page')
        if self.link_url is not None and self.link_category is not None:
            raise ValidationError('Select link url or link category')
        
       # if self.link_page is None and self.link_category is None:
            #raise ValidationError('Fill Just one')
        if self.link_url is None and self.link_category is None:
            raise ValidationError('Fill Just one')
        if self.link_page is None and self.link_url is None:
            raise ValidationError('Fill Just one')

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        if self.link_page is not None and self.link_category is not None:
            raise Exception('Select only one')
        if self.link_page is None and self.link_category is None:
            raise Exception('Select just one')
        if self.link_url is not None and self.link_page is not None:
            raise Exception('Select only one')
        if self.link_url is not None and self.link_category is not None:
            raise Exception('Select only one')

        return super().save()"""


@register_snippet
class Menu(ClusterableModel):

    
    title = models.CharField(max_length=100)
    slug = models.SlugField(
        verbose_name='slug',
        allow_unicode=True,
        max_length=255,
        null=True,
        )


    panels = [
        MultiFieldPanel([
            FieldPanel('title'),
            FieldPanel('slug'),
        ], heading='Menu'),
        InlinePanel('menu_items', label='Menu Item')
    ]

    def __str__(self):
        return self.title


@register_snippet
class FooterText(models.Model):
    title = models.CharField(max_length=255, blank=True)
    body = RichTextField()

    panels = [
        FieldPanel('title'),
        FieldPanel('body')
    ]

    def __str__(self):
        return 'Footer text'

    class Meta:
        verbose_name_plural = 'Footer Text'
