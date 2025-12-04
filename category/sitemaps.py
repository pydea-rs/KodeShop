from django.contrib.sitemaps import Sitemap
from category.models import Category

class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Category.objects.all()
    
    def lastmod(self, obj: Category):
        return obj.updated_at
    
    def location(self, obj: Category):
        return obj.url()