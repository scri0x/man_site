from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from man.views import page_not_found
from . import settings


urlpatterns = [
    path('captcha/', include('captcha.urls')),
    path('', include('man.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = page_not_found
