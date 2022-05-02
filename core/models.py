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
    open_in_new_tab = models.BooleanField(default=False, blank=True)

    page = ParentalKey('Menu', related_name='menu_items')


    panels = [
        FieldPanel('link_title'),
        FieldPanel('link_url'),
        PageChooserPanel('link_page'),
        FieldPanel('open_in_new_tab'),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return '#'

    @property
    def title(self):
        if self.link_page and not self.link_title:
            return self.link_page.title
        elif self.link_title:
            return self.link_title
        return 'Missing Title'




    """This is for the Validation"""
    
    def clean(self, *args, **kwargs):
        if not self.link_page and not self.link_url:
            msg = _('Please choose an internal page or custom URL')
            raise ValidationError({'link_page': msg})
        if self.link_url and self.link_page:
            msg = _('Linking to a page, and custom URL is not permitted')
            raise ValidationError({'link_page': msg, 'link_url':msg})
        if self.link_url and self.link_page:
            msg = _('Linking to a page and custom URL is not permitted')
            raise ValidationError({'link_page': msg, 'link_url':msg})
        if self.link_url and not self.link_title:
            msg = _('This field is required when linking to a custom URL')
            raise ValidationError({'link_title': msg})
        super().clean(*args, **kwargs)



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

    max_count = 1
    
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
