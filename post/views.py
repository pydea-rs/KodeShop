# views.py
from django.shortcuts import render
from .models import BlogPost, VideoPost
from django.shortcuts import render, get_object_or_404
from kodeshop.utils import PaginationParams


def show_blog(request, blog_id: int):
    from seo.utils import generate_article_schema
    from django.contrib.contenttypes.models import ContentType
    from seo.models import SEOMetadata
    
    blog = get_object_or_404(BlogPost, id=blog_id)
    
    # Get SEO metadata
    content_type = ContentType.objects.get_for_model(blog)
    try:
        seo_data = SEOMetadata.objects.get(content_type=content_type, object_id=blog.id)
    except SEOMetadata.DoesNotExist:
        seo_data = None
    
    # Generate schema markup
    schema_markup = generate_article_schema(blog)
    
    # Build breadcrumbs
    breadcrumbs = [
        {'name': 'خانه', 'url': '/'},
        {'name': 'بلاگ', 'url': '/posts/blogs/'},
        {'name': blog.title, 'url': blog.url()},
    ]
    
    context = {
        'blog': blog,
        'meta_title': blog.title[:60],
        'meta_description': blog.summary if blog.summary else blog.title,
        'og_type': 'article',
        'og_image': request.build_absolute_uri(blog.thumbnail.url) if blog.thumbnail else None,
        'schema_markup': schema_markup,
        'breadcrumbs': breadcrumbs,
        'seo_data': seo_data,
    }
    
    request.seo_object = blog
    
    return render(request, 'posts/blog.html', context)


def show_video(request, video_post_id: int):
    video = get_object_or_404(VideoPost, id=video_post_id)
    return render(request, 'posts/video.html', {'video': video})


def list_blog_posts(request):
    pagination = PaginationParams(request, BlogPost)
    blogs = pagination.get_items('created_at', order_descending=True)
    return render(request, 'posts/index.html', {'posts': blogs, 'pagination': pagination, })


def list_video_posts(request):
    pagination = PaginationParams(request, VideoPost)
    videos = pagination.get_items('created_at', order_descending=True)
    return render(request, 'posts/index.html', {'posts': videos, 'pagination': pagination, })