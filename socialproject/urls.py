from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

handler404 = 'customprofile.views.error404'
handler500 = 'customprofile.views.internal500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('profile/', include('customprofile.urls')),
    path('accounts/', include('allauth.urls')),
    path("robots.txt",TemplateView.as_view(template_name="customprofile/robots.txt", content_type="text/plain"),),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)