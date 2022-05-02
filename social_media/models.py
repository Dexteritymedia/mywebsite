from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images.edit_handlers import ImageChooserPanel

@register_setting
class SocialMediaSettings(BaseSetting):
    instagram = models.URLField(max_length=100, default='www.instagram.com/', null=True, blank=True, help_text='Instagram URL')
    facebook = models.URLField(max_length=100, default='www.facebook.com/', null=True, blank=True, help_text='Facebook URL')
    twitter = models.URLField(max_length=100, default='www.twitter.com/', null=True, blank=True, help_text='Twitter URL')
    pinterest = models.URLField(max_length=100, default='www.pinterest.com/', null=True, blank=True, help_text='Pinterest URL')
    linkedin = models.URLField(max_length=100, default='www.linkedin.com/', null=True, blank=True, help_text='Linkedin URL')
    whatsapp = models.CharField(max_length=100, default='Enter your WhatsApp number', null=True, blank=True, help_text='Whatsapp Number')
    
    panels = [
        MultiFieldPanel([
            
            FieldPanel('instagram'),
            FieldPanel('facebook'),
            FieldPanel('twitter'),
            FieldPanel('pinterest'),
            FieldPanel('linkedin'),
            FieldPanel('whatsapp'),
        ], heading="Social Media")
        ]

    class Meta:
        verbose_name = 'Social Media Channel'


@register_setting
class SiteSettings(BaseSetting):
    site_name = models.CharField(max_length=100, null=True, blank=True, help_text='Your website name')
    site_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        help_text='Your website logo',
        on_delete=models.CASCADE,
        related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)
    show_in_menu_bar = models.BooleanField(default=False, blank=True, help_text='Select to show logo in menu bar', verbose_name='Menu Logo',)
    show_title_in_menu_bar = models.BooleanField(default=False, blank=True, help_text='Select to show Title in menu bar', verbose_name='Menu Title',)

    panels = [
        MultiFieldPanel([
            FieldPanel('site_name'),
            FieldPanel('show_title_in_menu_bar'),
            ]),
        
        MultiFieldPanel([
            ImageChooserPanel('site_logo'),
            FieldPanel('show_in_menu_bar'),
            FieldPanel('caption'),
        ], heading="Website Image")
        

        ]

    class Meta:
        verbose_name = 'Site Setting'
