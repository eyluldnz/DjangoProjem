from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin

from content.models import Menu, Content, CImages


class ContentImageInline(admin.TabularInline):
    model = CImages
    extra = 2


class ContentAdmin(admin.ModelAdmin):
    list_display = ['title','type', 'image_tag', 'status', 'created_at']
    list_filter = ['status', 'type']
    inlines = [ContentImageInline]
    prepopulated_fields = {'slug': ('title',)}


class MenuAdmin(DraggableMPTTAdmin):
    mptt_intent_field= "title"
    list_display = ['tree_actions', 'indented_title','status']


admin.site.register(Menu,MenuAdmin)
admin.site.register(Content,ContentAdmin)
