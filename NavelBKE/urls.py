from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('account.urls')),
    path('accounts/', include('account.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('page.urls')),
    path('', include('story.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
