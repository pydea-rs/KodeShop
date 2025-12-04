from django.core.management.base import BaseCommand
from store.models import Product
from post.models import BlogPost
from seo.seo_analyzer import analyze_product_seo, analyze_blog_seo


class Command(BaseCommand):
    help = 'Audit SEO quality of content'

    def add_arguments(self, parser):
        parser.add_argument(
            '--type',
            type=str,
            choices=['products', 'blogs', 'all'],
            default='all',
            help='Type of content to audit'
        )
        parser.add_argument(
            '--limit',
            type=int,
            default=10,
            help='Number of items to audit'
        )

    def handle(self, *args, **options):
        content_type = options['type']
        limit = options['limit']
        
        self.stdout.write(self.style.SUCCESS('=== SEO Content Audit ===\n'))
        
        if content_type in ['products', 'all']:
            self.audit_products(limit)
        
        if content_type in ['blogs', 'all']:
            self.audit_blogs(limit)
    
    def audit_products(self, limit):
        self.stdout.write(self.style.WARNING('Auditing Products:'))
        products = Product.objects.all()[:limit]
        
        total_score = 0
        for product in products:
            result = analyze_product_seo(product)
            total_score += result['score']
            
            self.stdout.write(f"\n{product.name_fa}")
            self.stdout.write(f"  Score: {result['score']}/100 (Grade: {result['grade']})")
            
            if result['issues']:
                self.stdout.write("  Issues:")
                for issue in result['issues']:
                    self.stdout.write(f"    - {issue}")
        
        if products.count() > 0:
            avg_score = total_score / products.count()
            self.stdout.write(f"\nAverage Product SEO Score: {avg_score:.1f}/100")
    
    def audit_blogs(self, limit):
        self.stdout.write(self.style.WARNING('\nAuditing Blog Posts:'))
        blogs = BlogPost.objects.all()[:limit]
        
        total_score = 0
        for blog in blogs:
            result = analyze_blog_seo(blog)
            total_score += result['score']
            
            self.stdout.write(f"\n{blog.title}")
            self.stdout.write(f"  Score: {result['score']}/100 (Grade: {result['grade']})")
            
            if result['issues']:
                self.stdout.write("  Issues:")
                for issue in result['issues']:
                    self.stdout.write(f"    - {issue}")
        
        if blogs.count() > 0:
            avg_score = total_score / blogs.count()
            self.stdout.write(f"\nAverage Blog SEO Score: {avg_score:.1f}/100")
