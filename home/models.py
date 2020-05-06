from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm, TextInput, Textarea



class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'), ('False', 'Hayır'),
    )

    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    adress = models.CharField(blank=True, max_length=255)
    phone = models.CharField(blank=True, max_length=255)
    fax = models.CharField(blank=True, max_length=255)
    email = models.CharField(blank=True, max_length=255)
    stmpserver = models.CharField(max_length=25)
    stmpemail = models.CharField(max_length=25)
    stmppassword = models.CharField(max_length=25)
    stmpport = models.CharField(blank=True, max_length=10)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    aboutus = RichTextUploadingField(blank=True, )
    contact = RichTextUploadingField(blank=True, )
    references = RichTextUploadingField(blank=True, )
    status = models.CharField(max_length=10, choices=STATUS)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactFormMessage(models.Model):
    STATUS = (
        ('New', 'Yeni'), ('Read', 'Okundu'), ('Closed', 'Kapandı')
    )
    name = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=50)
    subject = models.CharField(blank=True, max_length=50)
    messages = models.CharField(blank=True, max_length=255)
    status = models.CharField(blank=True, choices=STATUS, max_length=50)
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactFormu(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name', 'email', 'subject', 'messages']
        widgets = {
            'name': TextInput(attrs={'class': 'input_field contact_form_name'}),
            'subject': TextInput(attrs={'class': 'input_field contact_form_name'}),
            'email': TextInput(attrs={'class': 'input_field contact_form_email'}),
            'messages':Textarea(attrs={'class': 'input_field contact_form_message','rows':'5'}),
        }
