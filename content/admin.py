from django.contrib import admin

# Register your models here.
from .models import Article, War, Era

admin.site.register(Article)
admin.site.register(War)
admin.site.register(Era)