from django.contrib import admin

# Register your models here.
from home.models import Setting, ContactFormMessage, UserProfil, Faq


class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name','email','note','messages','subject','status']
    list_filter = ['status']


class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']


class UserProfilAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'phone', 'adress', 'city', 'country','image_tag']


class FaqAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer','status']
    list_filter = ['status']


admin.site.register(ContactFormMessage,ContactFormMessageAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(UserProfil,UserProfilAdmin)
admin.site.register(Faq,FaqAdmin)