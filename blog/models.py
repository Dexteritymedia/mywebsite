from django.db import models
from django import forms
from django.utils import timezone
from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel

color = (
    ('', 'Select Title Color'),
    ('W', 'White'),
    ('B', 'Black'),
    ('R', 'Red')
)

class BlogPageCarousel(Orderable):

    page = ParentalKey('blog.BlogIndexPage', related_name='carousel_images',)
    carousel_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    carousel_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=False,
        related_name='+',
        on_delete=models.CASCADE,
        )
    carousel_title = models.CharField(max_length=250, null=True, blank=True, help_text="Add a Title")
    color = models.CharField(choices=color, max_length=100, blank=True, default='W', help_text='Change Text color')

    panels = [
        FieldPanel('carousel_title'),
        FieldPanel('color'),
        ImageChooserPanel('carousel_image'),
        PageChooserPanel('carousel_page'),
    ]


#to use auto select the title of the page when the page is selected

    @property
    def link(self):
        if self.carousel_page:
            return self.carousel_page.url
        return '#'

    @property
    def title(self):
        if self.carousel_page and not self.carousel_title:
            return self.carousel_page.title
        elif self.carousel_title:
            return self.carousel_title
        return 'Missing Title'

    @property
    def image(self):
        if self.carousel_page and not self.carousel_image:
            return self.carousel_page.image
        elif self.carousel_image:
            return self.carousel_image
        return 'Missing Image'


class BlogIndexPage(RoutablePageMixin, Page):
    template = "blog/blog_index.html"
    max_count = 0 #this shows how many pages can be created in this model which is 1
    
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="title"),
        MultiFieldPanel(
            [InlinePanel('carousel_images', max_num=3, min_num=1, label='Carousel',),
             ],
            heading='Carousel Images',
            classname='collapsible collapsed',
            ),
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        all_posts = BlogPage.objects.live().public().order_by('-first_published_at')
        #blogpages = self.get_children().live().order_by('-first_published_at')
        #context['blogpages'] = blogpages

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
        context['categories'] = BlogCategory.objects.all()
        return context

    

class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )



class BlogTagIndexPage(Page):
    template = "blog/blog_tag_index.html"
    max_count = 1

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context


class BlogCategoryIndexPage(Page):
    template = "blog/blog_category_index.html"
    max_count = 1

    def get_context(self, request):

        # Filter by tag
        """tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)"""

        # Update template context
        context = super().get_context(request)
        context['catgories'] = BlogCategory.objects.all()
        return context

    

class BlogPage(RoutablePageMixin, Page):
    template = "blog/blog_page.html"
    subpage_types = []
    parent_page_types = [
        'blog.BlogIndexPage'
        ]
    last_update = models.DateTimeField(default=timezone.now, verbose_name='Last Updated')
    date = models.DateField("Post date")
    subtitle = models.CharField(max_length=250, null=True, blank=True, help_text="You might add a Subtitle")
    body = RichTextField()
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )

        
    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
         MultiFieldPanel([
            FieldPanel('last_update'),
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Blog information"),
        InlinePanel('categories2', label="category", max_num=1),
        FieldPanel('subtitle'),
        FieldPanel('body', classname="full"),
        ImageChooserPanel('image'),
    ]


    def get_context(self, request):

        # Filter by tag
        related = BlogPage.objects.live().public().exclude(id=self.id).order_by('-first_published_at')[:3]
        #related = new.filter(categories__category__name=category)
        # Update template context
        #related = BlogPage.objects.live().public().filter(categories__name__contains=category).exclude(id=self.id).order_by('-first_published_at')[:3]
        context = super().get_context(request)
        context['related'] = related
        return context

    @route(r'^(?P<cat_slug>[-\w]*)/$', name='category_view')
    @route(r'^c/(?P<cat_slug>[-\w]*)/$', name='category_view')
    @route(r'^category/(?P<cat_slug>[-\w]*)/$', name='category_view')
    def category_view(self, request, cat_slug):
        context = self.get_context(request)

        try:
            category = BlogCategory.objects.get(slug=cat_slug)
        except Exception:
            category = None

        if category is None:
            pass

        context['posts'] = BlogPage.objects.live().public().filter(categories__in=[category])
        #context['posts'] = category
        return render(request, 'blog/blog_category_index.html', context)


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        verbose_name='slug',
        allow_unicode=True,
        max_length=255,
        null=True,
        )
    description = models.CharField(max_length=255, null=True, blank=True)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
        FieldPanel('description'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Blog Categories'
        ordering = ['name']


class BlogPageBlogCategory(models.Model):
    page = ParentalKey('blog.BlogPage', on_delete=models.CASCADE, related_name='categories2')
    blog_category = models.ForeignKey(
        'blog.BlogCategory', on_delete=models.CASCADE, related_name='blog_pages')

    panels = [
        SnippetChooserPanel('blog_category'),
        ]

    class Meta:
        unique_together = ('page', 'blog_category')
