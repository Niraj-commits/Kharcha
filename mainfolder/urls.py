from django.contrib import admin
from django.urls import path,include
from .sitemap import StaticViewSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    "static":StaticViewSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("tracker.urls")),
    path('',include('core.urls')),
    path('sitemap.xml',sitemap,{"sitemaps":sitemaps},name='sitemap'),
]
