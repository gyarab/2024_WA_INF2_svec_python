from django.contrib import admin
from django.urls import path
import content.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', content.views.homepage),
    path('article/<int:id>/', content.views.article),
    path('context/<int:id>/', content.views.context),
    path('tactics/<str:tactics_link>/', content.views.article_tactics),
    path('era/<int:id>', content.views.era),

]