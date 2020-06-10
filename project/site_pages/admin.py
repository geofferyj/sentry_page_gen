from django.contrib import admin
from site_pages.models import Page, MetaTag, CSS, ScriptTag

admin.site.register(Page)
admin.site.register(ScriptTag)
admin.site.register(MetaTag)
admin.site.register(CSS) 