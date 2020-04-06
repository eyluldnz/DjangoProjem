from django.contrib import admin

# Register your models here.
from home.models import Setting,ContactFormMessage

class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name','email','note','messages','subject','status']
    list_filter = ['status']
class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']

admin.site.register(Setting,SettingAdmin)
admin.site.register(ContactFormMessage,ContactFormMessageAdmin)