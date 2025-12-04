from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from post.models import BlogPost, VideoPost
from category.models import Category
from seo.models import SEOMetadata
from seo.utils import generate_product_schema, generate_article_schema


class Command(BaseCommand):
    help = 'Generate SEO metadata for all products, posts, and categories'

    def handle(self, *args, **options):
        self.stdout.write('Generating SEO metadata...')
        
        # Products
        products = Product.objects.all()
        for product in products:
            content_type = ContentType.objects.get_for_model(product)
            seo_meta, created = SEOMetadata.objects.get_or_create(
                content_type=content_type,
                object_id=product.id
            )
            
            if not seo_meta.meta_title:
                seo_meta.meta_title = f"{product.name_fa} - خرید آنلاین"
            
            if not seo_meta.meta_description:
                desc = product.description[:150] if product.description else f"خرید {product.name_fa} با بهترین قیمت"
                seo_meta.meta_description = desc
            
            if not seo_meta.meta_keywords:
                seo_meta.meta_keywords = f"{product.name_fa}, {product.category.name_fa}, خرید آنلاین"
            
            if not seo_meta.schema_markup:
                seo_meta.schema_markup = generate_product_schema(product)
            
            seo_meta.save()
            
            action = 'Created' if created else 'Updated'
            self.stdout.write(f'{action} SEO for product: {product.name_fa}')
        
        # Blog Posts
        blogs = BlogPost.objects.all()
        for blog in blogs:
            content_type = ContentType.objects.get_for_model(blog)
            seo_meta, created = SEOMetadata.objects.get_or_create(
                content_type=content_type,
                object_id=blog.id
            )
            
            if not seo_meta.meta_title:
                seo_meta.meta_title = blog.title[:60]
            
            if not seo_meta.meta_description:
                desc = blog.summary if blog.summary else blog.title
                seo_meta.meta_description = desc[:160]
            
            if not seo_meta.schema_markup:
                seo_meta.schema_markup = generate_article_schema(blog)
            
            seo_meta.save()
            
            action = 'Created' if created else 'Updated'
            self.stdout.write(f'{action} SEO for blog: {blog.title}')
        
        # Video Posts
        videos = VideoPost.objects.all()
        for video in videos:
            content_type = ContentType.objects.get_for_model(video)
            seo_meta, created = SEOMetadata.objects.get_or_create(
                content_type=content_type,
                object_id=video.id
            )
            
            if not seo_meta.meta_title:
                seo_meta.meta_title = video.title[:60]
            
            if not seo_meta.meta_description:
                desc = video.summary if video.summary else video.title
                seo_meta.meta_description = desc[:160]
            
            seo_meta.save()
            
            action = 'Created' if created else 'Updated'
            self.stdout.write(f'{action} SEO for video: {video.title}')
        
        # Categories
        categories = Category.objects.all()
        for category in categories:
            content_type = ContentType.objects.get_for_model(category)
            seo_meta, created = SEOMetadata.objects.get_or_create(
                content_type=content_type,
                object_id=category.id
            )
            
            if not seo_meta.meta_title:
                seo_meta.meta_title = f"{category.name_fa} - دسته بندی محصولات"
            
            if not seo_meta.meta_description:
                desc = category.description if category.description else f"مشاهده محصولات {category.name_fa}"
                seo_meta.meta_description = desc[:160]
            
            seo_meta.save()
            
            action = 'Created' if created else 'Updated'
            self.stdout.write(f'{action} SEO for category: {category.name_fa}')
        
        self.stdout.write(self.style.SUCCESS('Successfully generated SEO metadata!'))
