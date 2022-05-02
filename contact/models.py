from django.db import models

from modelcluster.fields import ParentalKey

# Create your models here.
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

from blog.models import BlogPage

class FormField(AbstractFormField):
    page = ParentalKey('FormPage', related_name='form_fields', on_delete=models.CASCADE)

class FormPage(AbstractEmailForm):

    template = 'contact_page.html'

    subpage_types = [
        #app_name.model,
        'contact.FormPage',
    ]
    parent_page_types = [
        'blog.BlogIndexPage',
    ]

    max_count = 3
    
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)
    use_other_template = models.BooleanField(null=True, blank=True, default='No', verbose_name='New Template', help_text='Use a different template',)

    def get_template(self, request, *args, **kwargs):
        if self.use_other_template:
            return 'subscribe_page.html'
        return 'contact_page.html'


    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('use_other_template'),
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('intro', classname='full'),
        FieldPanel('thank_you_text', classname='full'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname='col6'),
                FieldPanel('to_address', classname='col6'),
            ]),
            FieldPanel('subject'),
        ], heading='Email Settings'),
    ]
