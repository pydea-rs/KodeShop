from django.contrib.sitemaps import Sitemap
from .models import Product, Review


class ProductSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Product.objects.filter(available=True)

    def lastmod(self, obj: Product):
        return obj.modified
    
    def location(self, obj: Product):
        return obj.url()
