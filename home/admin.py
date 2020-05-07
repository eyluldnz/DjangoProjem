from django.contrib import admin

# Register your models here.
from home.models import Setting, ContactFormMessage, UserProfil


class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name','email','note','messages','subject','status']
    list_filter = ['status']
class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']
class UserProfilAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'phone','adress', 'city', 'country','image_tag']



admin.site.register(Setting,SettingAdmin)
admin.site.register(ContactFormMessage,ContactFormMessageAdmin)
admin.site.register(UserProfil,UserProfilAdmin)