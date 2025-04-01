from django.contrib import admin
from django.urls import path
import content.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', content.views.homepage),
    path('article/<int:id>/', content.views.article),
    path('war/<str:war>/', content.views.article_context),
    path('tactics/<str:tactics_link>/', content.views.article_tactics),
    path('war/<int:id>', content.views.war),
    path('era/<int:id>', content.views.era),
]
