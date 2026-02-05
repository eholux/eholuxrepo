from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Product


class ProductSitemap(Sitemap):
    """Sitemap for product pages"""
    changefreq = 'weekly'
    priority = 0.8
    
    def items(self):
        # Only include active products
        return Product.objects.filter(is_active=True)
    
    def lastmod(self, obj):
        return obj.updated_at
    
    def location(self, obj):
        return reverse('shop:product_detail', args=[obj.slug])
