from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from .models import Category, Book, Images, Comment

class BookImageInline(admin.TabularInline):
    model = Images
    extra = 2

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount','status','category','image_tag']
    readonly_fields = ('image_tag',)
    list_filter = ['status', 'category']
    inlines = [BookImageInline]




class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'book','image_tag']
    readonly_fields = ('image_tag',)

class CategoryAdmin1(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Book,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Book,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'


class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject','comment','book','user','status']
    list_filter = ['status']


admin.site.register(Category,CategoryAdmin1)
admin.site.register(Book,BookAdmin)
admin.site.register(Images,ImagesAdmin)
admin.site.register(Comment,CommentAdmin)