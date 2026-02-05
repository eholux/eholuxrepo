from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    """Sitemap for static pages"""
    priority = 1.0
    changefreq = 'monthly'
    
    def items(self):
        # Return list of view names
        return ['core:home', 'core:contact', 'core:faq', 'shop:shop', 'blog:blog_list']
    
    def location(self, item):
        return reverse(item)
