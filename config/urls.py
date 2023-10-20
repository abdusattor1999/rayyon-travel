from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
urlpatterns = i18n_patterns(
    path('admin-dashboard/', admin.site.urls, name="admin_dashboard"),
    path('account/', include("account.urls"), name='account'),
    path('', include("posts.urls"), name="posts"),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
