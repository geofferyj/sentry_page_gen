from django.db import models
from django.utils.text import  slugify
import random
import string

def gen_id(ln=5):
    ld = string.ascii_lowercase + string.digits
    return '-'+''.join((random.choice(ld) for i in range(ln)))


class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.slug:
            self.slug = self.slug
        else:
            self.slug = slugify(self.title) + gen_id()
        super().save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return self.title
 

class MetaTag(models.Model):
    name = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='meta_tags')
    

    def __str__(self):
        return self.name

class ScriptTag(models.Model):
    src = models.CharField(max_length=100, blank=True, null=True)
    body = models.CharField(max_length=400, blank=True, null=True)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='scripts')
    

    def __str__(self):
        return str(self.id)

class CSS(models.Model):
    rel = models.CharField(max_length=100, blank=True, null=True)
    href = models.CharField(max_length=400, blank=True, null=True)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='css')
    

    def __str__(self):
        return str(self.id)
