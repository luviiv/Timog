from django.conf.urls import patterns, include, url
from django.contrib import admin

from timog.sitemaps import BlogSitemap
from timog.sitemaps import StaticViewSitemap

admin.autodiscover()

sitemaps = {
    'blog': BlogSitemap,
    'static': StaticViewSitemap
}

urlpatterns = patterns('',
                       url(r'^$', 'apps.blog.views.index', name='home'),
                       url(r'^about$', 'apps.blog.views.about', name='about'),
                       url(r'^blog/', include('apps.blog.urls', namespace='blog')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'404', 'apps.blog.views.not_found'),
                       url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)
