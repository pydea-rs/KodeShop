from django.contrib.sitemaps import Sitemap
from post.models import BlogPost, VideoPost


class BlogPostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return BlogPost.objects.filter(is_visible=True).order_by('-created_at')

    def lastmod(self, obj: BlogPost):
        return obj.updated_at
    
    def location(self, obj: BlogPost):
        return obj.url()


class VideoPostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return VideoPost.objects.filter(is_visible=True).order_by('-created_at')

    def lastmod(self, obj: VideoPost):
        return obj.updated_at
    
    def location(self, obj: VideoPost):
        return obj.url()