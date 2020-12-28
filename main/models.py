from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class BlogPost(models.Model):
    title = models.CharField(max_length=120, null=True, blank=False)
    subtitle = models.CharField(max_length=180, null=True, blank=False)
    slug = models.CharField(max_length=240, null=True, blank=False)
    image = models.FileField(upload_to='article_img/',null=True, blank=False)
    body = HTMLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)