from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoryResources(resources.ModelResource):
    class Meta:
        model = Category

class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name','state',)
    resource_class = CategoryResources

class AuthorResources(resources.ModelResource):
    class Meta:
        model = Author 

class AuthorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['names', 'surnames', 'mail']
    list_display = ('names','surnames', 'mail', 'state', 'creation_date')
    resource_class = AuthorResources

admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post)
