from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.templatetags.wagtailcore_tags import richtext



class ImageBlock(blocks.StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """
    image = ImageChooserBlock(required=True)
    caption = blocks.CharBlock(required=False)
    attribution = blocks.CharBlock(required=False)
    shadow = blocks.ChoiceBlock(choices=[
        ('', 'Add Shadow'),
        ('S', 'Small Shadow'),
        ('R', 'Regular Shadow'),
        ('L', 'Larger Shadow')
    ], blank=True, required=False)
    
    class Meta:
        icon = 'image'
        template = "blocks/image_block.html"
        label = "Image"


class HeadingBlock(blocks.StructBlock):
    """
    Custom `StructBlock` that allows the user to select h2 - h4 sizes for headers
    """
    heading_text = blocks.CharBlock(classname="title", required=True)
    size = blocks.ChoiceBlock(choices=[
        ('', 'Select a header size'),
        ('h2', 'H2'),
        ('h3', 'H3'),
        ('h4', 'H4')
    ], blank=True, required=False)

    class Meta:
        icon = "title"
        template = "blocks/heading_block.html"
        label = "Heading"


class BlockQuote(blocks.StructBlock):
    """
    Custom `StructBlock` that allows the user to attribute a quote to the author
    """
    text = blocks.TextBlock()
    attribute_name = blocks.CharBlock(
        blank=True, required=False, label='e.g. Mary Berry')

    class Meta:
        icon = "openquote"
        template = "blocks/blockquote.html"
        label = "Block Quote"


class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True, help_text="Add additional text")


    class Meta:
        template = "blocks/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


class RichtextBlock(blocks.RichTextBlock):

    def get_api_representation(self, value, context=None):
        return richtext(value.source)


    class Meta:
        template = "blocks/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"



class SimpleRichtextBlock(blocks.RichTextBlock):

    def __init__(
        self, required=True, help_text=None, editor="default", features=None, **kwargs):
        super().__init__(**kwargs)
        self.features = ['bold','italic','link']


    class Meta:
        template = "blocks/richtext_block.html"
        icon = "edit"
        label = "Simple RichText"



class CTABlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.RichTextBlock(required=True, features=['bold','italic'])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True, default='Read More', max_length=40)


    class Meta:
        template = "blocks/cta_block.html"
        icon = "plus"
        label = "Call to Action"


class LinkStructValue(blocks.StructValue):

    def url(self):
        button_page = self.get('button_page')
        button_url = self.get('button_url')
        if button_page:
            return button_page.url
        elif button_url:
            return button_url

        return None


class ButtonBlock(blocks.StructBlock):
    button_page = blocks.PageChooserBlock(required=False, help_text='If selected, this url will be used first')
    button_url = blocks.URLBlock(required=False, help_text='If added, this url will be used secondarily to the button page')


    class Meta:
        template = "blocks/button_block.html"
        icon = "link"
        label = "Single Button"
        value_class = LinkStructValue



class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('image', ImageChooserBlock(required=True)),
                ('title', blocks.CharBlock(required=True, max_length=40)),
                ('text', blocks.TextBlock(required=True, max_length=200)),
                ('button_page', blocks.PageChooserBlock(required=False)),
                ('button_url', blocks.URLBlock(required=False, help_text='If the button page above is selected, that will be used first')),
            ]
        )
    )


    class Meta:
        template = "blocks/card_block.html"
        icon = "list-ul"
        label = "Cards"


class JumbotronBlock(blocks.StructBlock):

    jumbotron = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('image', ImageChooserBlock(required=False)),
                ('subtitle', blocks.CharBlock(required=False, max_length=40)),
                ('body', blocks.RichTextBlock(required=True, features=['h1','h2','h3','h4','h5','h6','hr','bold','italic','link'],)),
                ('color', blocks.CharBlock(required=False, max_length=40, help_text="Enter a hexdecimal color for the background e.g #000000")),
                ('button_page', blocks.PageChooserBlock(required=False)),
                ('button_url', blocks.URLBlock(required=False, help_text='If the button page above is selected, that will be used first')),
            ]
        )
    )


    class Meta:
        template = "blocks/jumbotron_block.html"
        icon = "list-ul"
        label = "Jumbotron"
        max_num = 1


class JumbotronBlockWithTextColor(blocks.StructBlock):

    jumbotron = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('image', ImageChooserBlock(required=False)),
                ('title', blocks.CharBlock(required=False, max_length=40)),
                ('description', blocks.RichTextBlock(required=False, features=['h1','h2','h3','h4','h5','h6','hr','bold','italic','link'],)),
                ('color', blocks.CharBlock(required=False, max_length=40, help_text="Enter a hexdecimal color for the background e.g #000000")),
                ('text_color', blocks.CharBlock(required=False, max_length=40, help_text="Enter a hexdecimal color for the text e.g #000000 or red")),
            ]
        )
    )


    class Meta:
        template = "blocks/jumbotron_text_block.html"
        icon = "list-ul"
        label = "Jumbotron"
        max_num = 1


class ContactBlock(blocks.StructBlock):
    select = blocks.BooleanBlock(required=False, blank=True, help_text='Select to use 2 columns', verbose_name='Two Columns',)
    background_color = blocks.CharBlock(required=False, max_length=60)
    title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.TextBlock(required=True)
    button_page = blocks.PageChooserBlock(required=False)
    image = ImageChooserBlock(required=False)
    button_text = blocks.CharBlock(required=False, default='Get in Touch', max_length=40)


    class Meta:
        template = "blocks/contact_block.html"
        label = "Contact"
        max_num = 1


class HomePageCardBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.TextBlock(required=True)
    button_page = blocks.PageChooserBlock(required=False)
    button_text = blocks.CharBlock(required=False, default='Enter', max_length=40)


    class Meta:
        template = "blocks/homepage_card_block.html"
        label = "Category"
        
"""
Navigation with Sub-Links

"""


class NavExternalLinkBlock(blocks.StructBlock):
    title = blocks.CharBlock(
        required=True,
        label='Title',
        max_length=200,
        )
    link = blocks.CharBlock(
        required=False,
        label='URL'
        )

    class Meta:
        template = 'blocks/external_link_block.html'
        label = 'External Link'


class NavPageLinkBlock(blocks.StructBlock):
    page = blocks.PageChooserBlock()


    class Meta:
        template = 'blocks/page_link_block.html'
        label = 'Page Link'
    

class NavSubLinkBlock(blocks.StructBlock):
    display_text = blocks.CharBlock(
        required=False,
        max_length=255,
    )
    sub_links = blocks.StreamBlock(

        [
            ('page_link', NavPageLinkBlock()),
            ('external_link', NavExternalLinkBlock()),
        ],
        required=False,
        label='Sub-links',
        )
        

class NavExternalLinkWithSubLinkBlock(NavSubLinkBlock, NavExternalLinkBlock):
    class Meta:
        label = 'External Link with sub-links'
    

class NavPageLinkWithSubLinkBlock(NavSubLinkBlock, NavPageLinkBlock):
    show_child_links = blocks.BooleanBlock(
        required=False,
        default=False,
        )

    class Meta:
        label = 'Page Link with sub-links'



    
class TOC(blocks.StructBlock):
    header = blocks.CharBlock(required=False)
    content = blocks.RichTextBlock(required=False)


    class Meta:
        template = "blocks/TOC.html"
        icon = "plus"
        label = "Article with TOC"


    
