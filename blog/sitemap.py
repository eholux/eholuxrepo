from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import BlogPost


class BlogPostSitemap(Sitemap):
    """Sitemap for blog post pages"""
    changefreq = 'monthly'
    priority = 0.7
    
    def items(self):
        # Include all blog posts
        return BlogPost.objects.all()
    
    def lastmod(self, obj):
        return obj.updated_at
    
    def location(self, obj):
        return reverse('blog:blog_detail', args=[obj.slug])
