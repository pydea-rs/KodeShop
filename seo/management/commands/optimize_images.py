from django.core.management.base import BaseCommand
from store.models import Product, Gallery
from post.models import BlogPost, VideoPost
from PIL import Image
import os


class Command(BaseCommand):
    help = 'Optimize images for better SEO and performance'

    def add_arguments(self, parser):
        parser.add_argument(
            '--max-width',
            type=int,
            default=1200,
            help='Maximum width for images'
        )
        parser.add_argument(
            '--quality',
            type=int,
            default=85,
            help='JPEG quality (1-100)'
        )

    def handle(self, *args, **options):
        max_width = options['max_width']
        quality = options['quality']
        
        self.stdout.write('Optimizing images...')
        
        optimized_count = 0
        
        # Optimize product images
        for product in Product.objects.all():
            if product.image:
                try:
                    if self.optimize_image(product.image.path, max_width, quality):
                        optimized_count += 1
                        self.stdout.write(f'Optimized: {product.name_fa}')
                except Exception as e:
                    self.stdout.write(self.style.WARNING(f'Failed to optimize {product.name_fa}: {str(e)}'))
        
        # Optimize gallery images
        for gallery_item in Gallery.objects.all():
            if gallery_item.image:
                try:
                    if self.optimize_image(gallery_item.image.path, max_width, quality):
                        optimized_count += 1
                except Exception as e:
                    pass
        
        # Optimize blog thumbnails
        for blog in BlogPost.objects.all():
            if blog.thumbnail:
                try:
                    if self.optimize_image(blog.thumbnail.path, max_width, quality):
                        optimized_count += 1
                except Exception as e:
                    pass
        
        self.stdout.write(self.style.SUCCESS(f'Successfully optimized {optimized_count} images!'))
    
    def optimize_image(self, image_path, max_width, quality):
        """
        Optimize a single image
        Returns True if optimized, False if skipped
        """
        if not os.path.exists(image_path):
            return False
        
        try:
            img = Image.open(image_path)
            
            # Skip if already small enough
            if img.width <= max_width:
                return False
            
            # Calculate new dimensions
            ratio = max_width / img.width
            new_height = int(img.height * ratio)
            
            # Resize
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            
            # Save with optimization
            if img.format == 'PNG':
                img.save(image_path, 'PNG', optimize=True)
            else:
                img.save(image_path, 'JPEG', quality=quality, optimize=True)
            
            return True
        except Exception as e:
            raise e
