# SEO Module for KodeShop

## Overview
Comprehensive SEO optimization module for Django e-commerce platform.

## Features

### 1. Dynamic SEO Metadata
- Meta titles, descriptions, keywords
- Open Graph tags (Facebook, LinkedIn)
- Twitter Cards
- Canonical URLs
- Robots directives (noindex, nofollow)

### 2. Schema.org Structured Data
- Product schema with ratings and pricing
- Article schema for blog posts
- Organization schema
- Website schema with search
- Breadcrumb schema

### 3. URL Management
- 301/302 redirects
- SEO-friendly slugs
- Canonical URL enforcement

### 4. Content Analysis
- SEO score calculator
- Keyword density checker
- Content length analyzer
- Image optimization checker

### 5. Management Commands
- `generate_seo_metadata` - Auto-generate SEO data
- `check_seo_health` - Audit SEO coverage
- `audit_seo` - Analyze content quality
- `optimize_images` - Compress and resize images

## Installation

1. Add to `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'seo',
]
```

2. Add middleware:
```python
MIDDLEWARE = [
    ...
    'seo.middleware.SEORedirectMiddleware',
    'seo.middleware.SecurityHeadersMiddleware',
]
```

3. Add context processor:
```python
TEMPLATES = [{
    'OPTIONS': {
        'context_processors': [
            ...
            'seo.context_processors.seo_metadata',
        ],
    },
}]
```

4. Run migrations:
```bash
python manage.py makemigrations seo
python manage.py migrate
```

## Usage

### In Views
```python
from seo.utils import generate_product_schema, get_or_create_seo_metadata

def product_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    
    # Get SEO metadata
    seo_meta = get_or_create_seo_metadata(product)
    
    # Generate schema
    schema = generate_product_schema(product)
    
    context = {
        'product': product,
        'schema_markup': schema,
        'meta_title': seo_meta.meta_title or product.name,
        'meta_description': seo_meta.meta_description,
    }
    return render(request, 'product.html', context)
```

### In Templates
```django
{% load seo_tags %}

<!-- Get SEO metadata -->
{% get_seo_metadata product as seo %}

<!-- Render schema markup -->
{% render_schema_markup schema_data %}

<!-- Get canonical URL -->
{% canonical_url as url %}
```

### In Admin
1. Go to `/panel/`
2. Navigate to "SEO" section
3. Edit metadata for any content
4. Create redirect rules

## Models

### SEOMetadata
Generic model for SEO data attached to any content.

Fields:
- `meta_title` - Page title (60 chars)
- `meta_description` - Page description (160 chars)
- `meta_keywords` - Keywords
- `og_title` - Open Graph title
- `og_description` - Open Graph description
- `og_image` - Social sharing image
- `canonical_url` - Canonical URL
- `noindex` - Prevent indexing
- `nofollow` - Prevent following links
- `schema_markup` - JSON-LD data

### RedirectRule
301/302 redirects for URL changes.

Fields:
- `old_path` - Original URL
- `new_path` - New URL
- `redirect_type` - 301 or 302
- `is_active` - Enable/disable

## Management Commands

### Generate SEO Metadata
```bash
python manage.py generate_seo_metadata
```
Auto-generates SEO metadata for all products, posts, and categories.

### Check SEO Health
```bash
python manage.py check_seo_health
```
Audits SEO coverage and identifies issues.

### Audit Content
```bash
python manage.py audit_seo --type=products --limit=10
```
Analyzes content quality and provides SEO scores.

### Optimize Images
```bash
python manage.py optimize_images --max-width=1200 --quality=85
```
Compresses and resizes images for better performance.

## Template Tags

### get_seo_metadata
```django
{% get_seo_metadata object as seo %}
{{ seo.meta_title }}
```

### render_schema_markup
```django
{% render_schema_markup schema_dict %}
```

### canonical_url
```django
{% canonical_url as url %}
<link rel="canonical" href="{{ url }}">
```

### truncate_seo
```django
{{ text|truncate_seo:160 }}
```

## Utilities

### Schema Generators
```python
from seo.utils import (
    generate_product_schema,
    generate_article_schema,
    generate_breadcrumb_schema,
    generate_organization_schema,
)

# Product schema
schema = generate_product_schema(product)

# Article schema
schema = generate_article_schema(blog_post)

# Breadcrumbs
breadcrumbs = [('Home', '/'), ('Products', '/store/')]
schema = generate_breadcrumb_schema(breadcrumbs)
```

### SEO Analyzer
```python
from seo.seo_analyzer import SEOAnalyzer

analyzer = SEOAnalyzer(
    content=blog.body,
    title=blog.title,
    description=blog.summary,
    focus_keyword='farming tools'
)

result = analyzer.analyze()
print(f"Score: {result['score']}/100")
print(f"Grade: {result['grade']}")
print(f"Issues: {result['issues']}")
```

## Configuration

Add to `settings.py`:
```python
# SEO Configuration
SEO_SITE_NAME = 'KodeShop'
SEO_SITE_DESCRIPTION = 'فروشگاه آنلاین ابزار کشاورزی'
SEO_DEFAULT_IMAGE = '/static/images/og-default.jpg'
SEO_TWITTER_HANDLE = '@kodeshop'

# Security Headers
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'SAMEORIGIN'
```

## Best Practices

1. **Unique Titles**: Each page should have a unique title
2. **Compelling Descriptions**: Write engaging meta descriptions
3. **Keywords**: Use keywords naturally, avoid stuffing
4. **Images**: Always include alt text
5. **Content**: Aim for 600+ words on important pages
6. **Links**: Include internal links to related content
7. **Mobile**: Ensure mobile responsiveness
8. **Speed**: Optimize images and enable caching

## Testing

### Test Schema Markup
- Google Rich Results Test: https://search.google.com/test/rich-results
- Schema.org Validator: https://validator.schema.org/

### Test Meta Tags
- Facebook Debugger: https://developers.facebook.com/tools/debug/
- Twitter Card Validator: https://cards-dev.twitter.com/validator

### Test Performance
- Google PageSpeed: https://pagespeed.web.dev/
- GTmetrix: https://gtmetrix.com/

## Troubleshooting

### Sitemap not showing
```bash
python manage.py migrate
# Visit /sitemap.xml
```

### SEO metadata not appearing
```bash
python manage.py generate_seo_metadata
# Clear browser cache
```

### Schema errors
- Validate at https://validator.schema.org/
- Check JSON syntax
- Ensure required fields are present

## Contributing

When adding new content types:
1. Add SEO fields to model
2. Create schema generator in `utils.py`
3. Update views to include SEO context
4. Add to `generate_seo_metadata` command

## License

Part of KodeShop project.

## Support

For issues or questions, check:
- `SEO_GUIDE.md` - Comprehensive guide
- `SEO_QUICK_START.md` - Quick setup
- `SEO_CHECKLIST.md` - Implementation checklist
