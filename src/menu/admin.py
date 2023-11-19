from django.contrib import admin

from .models import Menu, MenuItem


@admin.register(Menu)
class TreeMenuCategoryAdmin(admin.ModelAdmin):

    fields = ('name', 'slug')
    list_display = ('name', 'slug')


@admin.register(MenuItem)
class TreeMenuAdmin(admin.ModelAdmin):

    fields = ('name', 'category', 'slug', 'parent')
    list_display = ('name', 'category', 'slug', 'parent')
