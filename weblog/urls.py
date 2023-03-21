from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('api/', include('api.urls')),
    path('blog/', include('blog.urls')),
    path('resume/', include('resume.urls')),
    path('account/', include('account.urls')),
    path('contact_us/', include('contact_us.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)