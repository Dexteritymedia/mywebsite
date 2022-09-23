from wagtail.core import hooks
from wagtail.contrib.modeladmin.options import ( ModelAdmin, ModelAdminGroup, modeladmin_register)
from blog.models import BlogPage, KnowledgeBase
from flex.models import FlexPage
from contact.models import FormPage
from chart.models import DataPage, DataListingPage

#to change the name "Snippets" to Overview in wagtail admin sidebar
@hooks.register('construct_main_menu')
def change_page_name(request, menu_items):
    for item in menu_items:
        if item.__class__.__name__=='SnippetsMenuItem':
            item.label = 'Snippets'


class BlogAdmin(ModelAdmin):
    model = BlogPage
    menu_label = 'Blog Posts'
    menu_icon = 'doc-empty-inverse'
    menu_order = 150
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('title', 'date', 'last_update')
    search_fields = ('title', 'body')

modeladmin_register(BlogAdmin)

class FlexAdmin(ModelAdmin):
    model = FlexPage
    menu_label = 'Pages'
    menu_icon = 'folder-inverse'
    menu_order = 170
    add_to_seetings_menu = False
    exclude_from_explorer = False
    search_fields = ('title', 'subtitle', 'content')

modeladmin_register(FlexAdmin)

class KnowledgeBaseAdmin(ModelAdmin):
    model = KnowledgeBase
    menu_label = 'KnowledgeBase'
    menu_icon = 'group'
    menu_order = 180
    add_to_seetings_menu = False
    exclude_from_explorer = False
    #list_display = ('date')
    search_fields = ('body')

modeladmin_register(KnowledgeBaseAdmin)

class FormAdmin(ModelAdmin):
    model = FormPage
    menu_label = 'Contact Forms'
    menu_icon = 'list-ul'
    menu_order = 600
    add_to_seetings_menu = False
    exclude_from_explorer = False

modeladmin_register(FormAdmin)

class DataAdmin(ModelAdmin):
    model = DataPage
    menu_label = 'Data Posts'
    menu_icon = 'list-ul'
    menu_order = 160
    add_to_seetings_menu = False
    exclude_from_explorer = False
    list_display = ('title', 'date',)
    search_fields = ('title', 'body')

modeladmin_register(DataAdmin)


class DataListingAdmin(ModelAdmin):
    model = DataListingPage
    menu_label = 'Data Categories'
    #menu_icon = 'list-ul'
    menu_order = 165
    add_to_seetings_menu = False
    exclude_from_explorer = False
    list_display = ('title',)
    search_fields = ('title')

modeladmin_register(DataListingAdmin)

#to change the name "Pages" to Overview in wagtail admin sidebar
@hooks.register('construct_main_menu')
def change_page_name(request, menu_items):
    for item in menu_items:
        if item.__class__.__name__=='ExplorerMenuItem':
            item.label = 'Overview'

