from django.db import models
from django import forms
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from core import blocks

color = (
    ('', 'Select Title Color'),
    ('W', 'White'),
    ('B', 'Black'),
    ('R', 'Red')
)

class BlogPageCarousel(Orderable):

    page = ParentalKey('blog.BlogIndexPage', related_name='carousel_images', blank=True)
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
        blank=True,
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
    max_count = 1 #this shows how many pages can be created in this model which is 1
    
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


    @route(r'^(\d{4})/(\d{2})/(\d{2})/(.+)/$', name='post_view')
    def post_by_date_slug(self, request, year, month, day, slug, *args, **kwargs):
        post_page = self.get_posts().filter(slug=slug).first()
        if not post_page:
            raise Http404
        return post_page.serve(request)

    

class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )



class BlogTagIndexPage(Page):
    template = "blog/blog_tag_index.html"
    max_count = 1

    subpage_types = ['blog.BlogPage']
    parent_page_types = [
        'blog.BlogListingPage'
        ]

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context



class BlogListingPage(RoutablePageMixin, Page):
    template = "blog/blog_listing_page.html"
    max_count = 10 #this shows how many pages can be created in this model which is 10

    subpage_types = ['blog.BlogPage']
    parent_page_types = [
        'blog.BlogIndexPage'
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


    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = BlogListingPage.get_children(self,).live().order_by('-first_published_at')
        all_posts = BlogPage.objects.live().public().order_by('-first_published_at')

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

    

class BlogPage(RoutablePageMixin, Page):
    template = "blog/blog_page.html"
    subpage_types = []
    parent_page_types = [
        'blog.BlogListingPage'
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


    def get_posts(self, category=None):
        posts = BlogPage.objects.live().descendant_of(self)
        if category:
            posts = posts.filter(categories=category)
        return posts

   

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


class KnowledgeBaseIndex(Page):

    template = 'knowledgebase.html'

    subpage_types = [
        'blog.KnowledgeBase'
        ]
    parent_page_types = [
        'blog.BlogIndexPage',
    ]

    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        #FieldPanel('tags'),
    ]

    class Meta:
        verbose_name = 'KnowledgeBase'
        verbose_name_plural = 'KnowledgeBase'


    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        all_posts = KnowledgeBase.objects.live().public().order_by('-first_published_at')


        paginator = Paginator(all_posts, 1)

        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context['posts'] = posts
        return context



class KnowledgeBase(Page):

    template = 'knowledgebase_page.html'

    subpage_types = []
    parent_page_types = [
        'blog.KnowledgeBaseIndex',
    ]
    
    date = models.DateTimeField(default=timezone.now, verbose_name='Date')
    body = RichTextField()
    #tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body', classname="full"),
        #FieldPanel('tags'),
    ]

        
    class Meta:
        verbose_name = 'KnowledgeBase'
        verbose_name_plural = 'KnowledgeBase'


    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        all_posts = KnowledgeBase.objects.live().public().order_by('-first_published_at')


        paginator = Paginator(all_posts, 1)

        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context['posts'] = posts
        return context



"""
KnowledgeBase._meta.get_field('title').blank=True
KnowledgeBase._meta.get_field('title').default='KnowledgeBase'
KnowledgeBase._meta.get_field('slug').default='knowledgeBase'
"""
