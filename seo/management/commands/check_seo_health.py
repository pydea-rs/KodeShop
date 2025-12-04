from django.core.management.base import BaseCommand
from store.models import Product
from post.models import BlogPost, VideoPost
from category.models import Category
from django.contrib.contenttypes.models import ContentType
from seo.models import SEOMetadata


class Command(BaseCommand):
    help = 'Check SEO health of the website'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('=== SEO Health Check ===\n'))
        
        # Check Products
        products = Product.objects.all()
        products_with_seo = 0
        products_missing_meta = []
        
        for product in products:
            content_type = ContentType.objects.get_for_model(product)
            try:
                seo_meta = SEOMetadata.objects.get(content_type=content_type, object_id=product.id)
                if seo_meta.meta_title and seo_meta.meta_description:
                    products_with_seo += 1
                else:
                    products_missing_meta.append(product.name_fa)
            except SEOMetadata.DoesNotExist:
                products_missing_meta.append(product.name_fa)
        
        self.stdout.write(f'Products: {products_with_seo}/{products.count()} have complete SEO metadata')
        if products_missing_meta:
            self.stdout.write(self.style.WARNING(f'  Missing: {", ".join(products_missing_meta[:5])}...'))
        
        # Check Blog Posts
        blogs = BlogPost.objects.all()
        blogs_with_seo = 0
        
        for blog in blogs:
            content_type = ContentType.objects.get_for_model(blog)
            try:
                seo_meta = SEOMetadata.objects.get(content_type=content_type, object_id=blog.id)
                if seo_meta.meta_title and seo_meta.meta_description:
                    blogs_with_seo += 1
            except SEOMetadata.DoesNotExist:
                pass
        
        self.stdout.write(f'Blog Posts: {blogs_with_seo}/{blogs.count()} have complete SEO metadata')
        
        # Check Categories
        categories = Category.objects.all()
        categories_with_seo = 0
        
        for category in categories:
            content_type = ContentType.objects.get_for_model(category)
            try:
                seo_meta = SEOMetadata.objects.get(content_type=content_type, object_id=category.id)
                if seo_meta.meta_title and seo_meta.meta_description:
                    categories_with_seo += 1
            except SEOMetadata.DoesNotExist:
                pass
        
        self.stdout.write(f'Categories: {categories_with_seo}/{categories.count()} have complete SEO metadata')
        
        # Check for missing slugs
        products_no_slug = Product.objects.filter(slug='').count()
        if products_no_slug > 0:
            self.stdout.write(self.style.ERROR(f'\n⚠ {products_no_slug} products missing slugs!'))
        
        # Check for missing descriptions
        products_no_desc = Product.objects.filter(description='').count()
        if products_no_desc > 0:
            self.stdout.write(self.style.WARNING(f'⚠ {products_no_desc} products missing descriptions'))
        
        # Check for missing images
        products_no_image = Product.objects.filter(image='').count()
        if products_no_image > 0:
            self.stdout.write(self.style.WARNING(f'⚠ {products_no_image} products missing images'))
        
        # Summary
        total_items = products.count() + blogs.count() + categories.count()
        total_with_seo = products_with_seo + blogs_with_seo + categories_with_seo
        percentage = (total_with_seo / total_items * 100) if total_items > 0 else 0
        
        self.stdout.write(f'\n=== Overall SEO Coverage: {percentage:.1f}% ===')
        
        if percentage < 50:
            self.stdout.write(self.style.ERROR('⚠ SEO coverage is low! Run: python manage.py generate_seo_metadata'))
        elif percentage < 80:
            self.stdout.write(self.style.WARNING('⚠ SEO coverage needs improvement'))
        else:
            self.stdout.write(self.style.SUCCESS('✓ Good SEO coverage!'))
