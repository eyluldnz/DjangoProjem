from django.db import models
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    #açılan kutu için:
    STATUS = (
        ('True', 'Evet'),('False','Hayır'),
    )
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True,upload_to='images/')
    status = models.CharField(max_length=10,choices=STATUS)

    slug = models.SlugField()
    parent= TreeForeignKey('self', blank=True,null=True,  related_name='children', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
          full_path =[self.title]
          k=self.parent
          while k is not None:
               full_path.append(k.title)
               k=k.parent
          return '->'.join(full_path[::-1])





class Book(models.Model):
    # açılan kutu için:
    STATUS = (
        ('True', 'Evet'), ('False', 'Hayır'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # categori ile ilişki kuruluyor
    title = models.CharField(max_length=150)
    author=models.CharField(max_length=255)
    dates=models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True,null=True, upload_to='images/')
    detail = RichTextUploadingField()
    status = models.CharField(max_length=10, choices=STATUS)
    amount = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<image src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'



class Images(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<image src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'


