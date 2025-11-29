from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['home','add_card','login', 'register','logout']  # url names

    def location(self, item):
        return reverse(item)
