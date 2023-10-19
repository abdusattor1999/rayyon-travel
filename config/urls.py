from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin-dashboard/', admin.site.urls, name="admin_dashboard"),
    path('account/', include("account.urls")),
    path('', include("posts.urls"), name="posts"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
