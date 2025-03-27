from django.contrib import admin

# Register your models here.
from .models import Article, War, Tactics

admin.site.register(Article)
admin.site.register(War)
admin.site.register(Tactics)