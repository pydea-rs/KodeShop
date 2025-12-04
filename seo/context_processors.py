from django.contrib.contenttypes.models import ContentType
from .models import SEOMetadata


def seo_metadata(request):
    """
    Context processor to make SEO metadata available in templates
    """
    context = {
        'seo_data': None,
        'page_url': request.build_absolute_uri(),
    }
    
    # Try to get SEO metadata for the current view
    try:
        view_name = request.resolver_match.view_name
        # This will be populated by views when they set request.seo_object
        if hasattr(request, 'seo_object') and request.seo_object:
            content_type = ContentType.objects.get_for_model(request.seo_object)
            try:
                seo_data = SEOMetadata.objects.get(
                    content_type=content_type,
                    object_id=request.seo_object.id
                )
                context['seo_data'] = seo_data
            except SEOMetadata.DoesNotExist:
                pass
    except:
        pass
    
    return context
