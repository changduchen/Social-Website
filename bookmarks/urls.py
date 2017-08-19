"""bookmarks URL Configuration"""

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='account/dashboard.html'), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('account.urls')),
    url('social-auth/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^images/', include('images.urls', namespace='images')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
