from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):

    def items(self):
        return ['login','home','add_card', 'register','logout']  # url names

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        if item == 'login':
            return 1.0
        return 0.8

    def changefreq(self, item):
        if item == 'login':
            return 'daily'
        return 'weekly'