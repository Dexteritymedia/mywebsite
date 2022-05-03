from django import template

from ..models import FormPage

register = template.Library()


@register.inclusion_tag('subscribe_page.html', takes_context=True)
def subscribe(context):
    try:
        page = FormPage.objects.get(slug='subscribe')
    except FormPage.DoesNotExist:
        page = None
    

    return {
        'page': page,
        'form': page.get_form(),
        'request': context['request'],
    }
