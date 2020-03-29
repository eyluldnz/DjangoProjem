from django.contrib import admin


from .models import Category, Book, Images

class BookImageInline(admin.TabularInline):
    model = Images
    extra = 2

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount','status','category','image_tag']
    readonly_fields = ('image_tag',)
    list_filter = ['status','category']
    inlines = [BookImageInline]



class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'book','image']
admin.site.register(Category,CategoryAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Images,ImagesAdmin)