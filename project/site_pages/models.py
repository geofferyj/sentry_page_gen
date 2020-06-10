from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

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
