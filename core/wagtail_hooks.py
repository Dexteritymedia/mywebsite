from wagtail.contrib.modeladmin.options import ( ModelAdmin, ModelAdminGroup, modeladmin_register)
from blog.models import BlogPage
from flex.models import FlexPage


class BlogAdmin(ModelAdmin):
    model = BlogPage
    menu_label = 'Blog Posts'
    menu_icon = 'doc-empty-inverse'
    menu_order = 50
    add_to_seetings_menu = False
    exclude_from_explorer = False
    list_display = ('title', 'date', 'last_update')
    #list_filter = ('author')
    search_fields = ('title', 'body')

modeladmin_register(BlogAdmin)

class FlexAdmin(ModelAdmin):
    model = FlexPage
    menu_label = 'Flex Pages'
    menu_icon = 'folder-inverse'
    menu_order = 70
    add_to_seetings_menu = False
    exclude_from_explorer = False
    search_fields = ('title', 'subtitle', 'content')

modeladmin_register(FlexAdmin)


"""

class PostAdmin(ModelAdmin):
    model = Flex
    menu_label = 'Posts'
    menu_icon = 'doc-empty-inverse'
    menu_order = 100
    add_to_seetings_menu = False
    exclude_from_explorer = False
    list_display = ('title', 'author')
    #list_filter = ('author')
    search_fields = ('title', 'author')

modeladmin_register(PostAdmin)
"""
