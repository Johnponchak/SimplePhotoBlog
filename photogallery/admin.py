from django.contrib import admin
from .models import Gallery, GalleryImage, Archive
# Register your models here.

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'archive')

class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'gallery', 'caption')

class ArchiveAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(Archive, ArchiveAdmin)