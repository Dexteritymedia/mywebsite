from django import template

from ..models import Menu, FooterText

register = template.Library()

@register.simple_tag()
def get_menu(slug):
    return Menu.objects.filter(slug=slug).first()


@register.inclusion_tag('include/footer_text.html', takes_context=True)
def get_footer_text(context):
    footer_text = ''
    if FooterText.objects.first() is not None:
        footer_text = FooterText.objects.first().body


    return {
        'footer_text': footer_text,
    }
