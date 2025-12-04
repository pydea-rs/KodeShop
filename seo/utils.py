from django.contrib.contenttypes.models import ContentType
from .models import SEOMetadata


def generate_product_schema(product):
    """
    Generate Product schema markup for rich snippets
    """
    schema = {
        "@context": "https://schema.org/",
        "@type": "Product",
        "name": product.name_fa,
        "image": [product.image.url] if product.image else [],
        "description": product.description[:200] if product.description else "",
        "sku": str(product.id),
        "brand": {
            "@type": "Brand",
            "name": "KodeShop"
        },
        "offers": {
            "@type": "Offer",
            "url": product.url(),
            "priceCurrency": "IRR",
            "price": str(product.price),
            "availability": "https://schema.org/InStock" if product.available and product.stock > 0 else "https://schema.org/OutOfStock",
        }
    }
    
    # Add rating if available
    rating = product.rating()
    if rating:
        from store.models import Review
        review_count = Review.objects.filter(product=product, status=True).count()
        schema["aggregateRating"] = {
            "@type": "AggregateRating",
            "ratingValue": str(rating),
            "reviewCount": str(review_count)
        }
    
    return schema


def generate_article_schema(blog_post):
    """
    Generate Article schema markup for blog posts
    """
    schema = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": blog_post.title,
        "description": blog_post.summary if blog_post.summary else blog_post.title,
        "datePublished": blog_post.created_at.isoformat(),
        "dateModified": blog_post.updated_at.isoformat(),
    }
    
    if blog_post.thumbnail:
        schema["image"] = blog_post.thumbnail.url
    
    if blog_post.author:
        schema["author"] = {
            "@type": "Person",
            "name": f"{blog_post.author.fname} {blog_post.author.lname}"
        }
    
    return schema


def generate_breadcrumb_schema(breadcrumbs):
    """
    Generate BreadcrumbList schema
    breadcrumbs should be a list of tuples: [(name, url), ...]
    """
    items = []
    for position, (name, url) in enumerate(breadcrumbs, start=1):
        items.append({
            "@type": "ListItem",
            "position": position,
            "name": name,
            "item": url
        })
    
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items
    }


def generate_organization_schema():
    """
    Generate Organization schema for the website
    """
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "KodeShop",
        "url": "https://kode.mehrzadco.com",
        "logo": "https://kode.mehrzadco.com/static/images/logo.png",
        "description": "فروشگاه آنلاین ابزار و تجهیزات کشاورزی",
        "contactPoint": {
            "@type": "ContactPoint",
            "contactType": "customer service",
            "availableLanguage": ["Persian", "English"]
        }
    }


def get_or_create_seo_metadata(obj):
    """
    Get or create SEO metadata for an object
    """
    content_type = ContentType.objects.get_for_model(obj)
    seo_meta, created = SEOMetadata.objects.get_or_create(
        content_type=content_type,
        object_id=obj.id
    )
    return seo_meta
