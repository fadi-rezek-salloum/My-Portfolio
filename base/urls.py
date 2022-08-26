from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('administrator/authorization-handler/', admin.site.urls),

    path('', include('main.urls', namespace='main')),
    path('projects/', include('projects.urls', namespace='projects')),
    path('contact', include('contact.urls', namespace='contact')),
]

handler404 = 'main.views.error_404_view'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)