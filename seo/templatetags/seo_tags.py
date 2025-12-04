from django import template
from django.utils.safestring import mark_safe
from django.contrib.contenttypes.models import ContentType
from seo.models import SEOMetadata
import json

register = template.Library()


@register.simple_tag
def get_seo_metadata(obj):
    """
    Get SEO metadata for any object
    Usage: {% get_seo_metadata product as seo %}
    """
    try:
        content_type = ContentType.objects.get_for_model(obj)
        return SEOMetadata.objects.get(content_type=content_type, object_id=obj.id)
    except SEOMetadata.DoesNotExist:
        return None


@register.simple_tag
def render_schema_markup(schema_data):
    """
    Render JSON-LD schema markup
    Usage: {% render_schema_markup schema_dict %}
    """
    if schema_data:
        return mark_safe(f'<script type="application/ld+json">{json.dumps(schema_data, ensure_ascii=False)}</script>')
    return ''


@register.simple_tag(takes_context=True)
def canonical_url(context):
    """
    Generate canonical URL
    """
    request = context.get('request')
    if request:
        return request.build_absolute_uri(request.path)
    return ''


@register.filter
def truncate_seo(text, length=160):
    """
    Truncate text for SEO meta descriptions
    """
    if len(text) <= length:
        return text
    return text[:length-3] + '...'
