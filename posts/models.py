from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import time
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings
from ckeditor.fields import RichTextField

class Category(models.Model):
    category_name = models.CharField(max_length=200, blank=True)
    category_image = ProcessedImageField(upload_to='card-background', blank=True, null=True)

    def __str__(self):
   	 return self.category_name

    class Meta:
   	 verbose_name_plural = "Categories"

class Type(models.Model):
    type_name = models.CharField(max_length=200, blank=True)

    def __str__(self):
   	 return self.type_name

    class Meta:
   	 verbose_name_plural = "Types"

class Articles(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length = 40)
    summary = models.CharField(max_length = 140)
    description = models.TextField(max_length = 2500, blank = True, null = True)
    cover = ProcessedImageField(upload_to='images', format= 'PNG', blank=True, null=True)
    typename = models.ForeignKey(Type , on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
   	 return self.title

    class Meta:
   	 verbose_name_plural = "Articles"

class Comment(models.Model):

  article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='comments')
  user = models.CharField(max_length=200)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
  # approved_comment = models.BooleanField(default=False)

  # def approve(self):
  #   self.approved_comment = True
  #   self.save()

  def __str__(self):
    return self.text
    