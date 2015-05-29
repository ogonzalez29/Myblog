# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import BlogPost, Categorias

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'time', 'status', 'author', 'admin_categorias')
    list_instances = True
    search_fields = ['title'] 

admin.site.register(BlogPost, BlogPostAdmin)

class CategoriasAdmin(admin.ModelAdmin):
#Sets up values fow how admin site lists categories
	list_display = ('nombre', 'creada_en', 'actualizada_al')
	list_display_links = ('nombre', 'creada_en', 'actualizada_al')
	list_per_page = 20
	ordering = ['nombre']
	search_fields = ['nombre', 'descripcion']

#Sets up slug to be generated from category name
	prepopulated_fields = {'slug': ('nombre',)}

#Class to filter by categories, NOT WORKING!!!
class CategoriasAdminFilter(admin.ModelAdmin):
	model = Categorias
	list_filter = ['blogpost__nombre']

admin.site.register(Categorias, CategoriasAdmin)
