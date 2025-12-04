from django.core.management.base import BaseCommand
from django.conf import settings
import os


class Command(BaseCommand):
    help = 'Generate a sitemap index file for better SEO'

    def handle(self, *args, **options):
        sitemap_index = """<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <sitemap>
        <loc>https://kode.mehrzadco.com/sitemap.xml</loc>
    </sitemap>
</sitemapindex>
"""
        
        # Write to static directory
        static_root = settings.STATIC_ROOT
        if not os.path.exists(static_root):
            os.makedirs(static_root)
        
        sitemap_path = os.path.join(static_root, 'sitemap_index.xml')
        
        with open(sitemap_path, 'w', encoding='utf-8') as f:
            f.write(sitemap_index)
        
        self.stdout.write(self.style.SUCCESS(f'Sitemap index created at: {sitemap_path}'))
        self.stdout.write('Submit this to Google Search Console and Bing Webmaster Tools')
