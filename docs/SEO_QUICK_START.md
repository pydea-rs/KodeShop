# SEO Quick Start Guide

## 🚀 Quick Setup (5 minutes)

### 1. Run Setup Script
```bash
chmod +x setup_seo.sh
./setup_seo.sh
```

Or manually:
```bash
python manage.py makemigrations seo
python manage.py migrate
python manage.py generate_seo_metadata
```

### 2. Update .env File
Add these lines to your `.env`:
```
SEO_SITE_NAME=KodeShop
SEO_SITE_DESCRIPTION=فروشگاه آنلاین ابزار و تجهیزات کشاورزی
SEO_TWITTER_HANDLE=@kodeshop
```

### 3. Verify Installation
```bash
python manage.py check_seo_health
```

## 📊 What Was Implemented

### ✅ Technical SEO
- XML Sitemaps (products, blogs, categories)
- Robots.txt configuration
- Canonical URLs
- 301/302 redirects
- Security headers
- Schema.org structured data

### ✅ On-Page SEO
- Meta titles and descriptions
- Open Graph tags (Facebook, LinkedIn)
- Twitter Cards
- Breadcrumb navigation
- SEO-friendly URLs
- Image optimization

### ✅ Content SEO
- Product schema with ratings
- Blog article schema
- Organization schema
- Website search schema
- Breadcrumb schema

## 🎯 Priority Actions

### Immediate (Do Now):
1. ✅ Run migrations (done by setup script)
2. ✅ Generate SEO metadata (done by setup script)
3. 📝 Review metadata in admin: `/panel/` → SEO section
4. 🔍 Submit sitemap to Google: https://search.google.com/search-console
5. 🔍 Submit sitemap to Bing: https://www.bing.com/webmasters

### This Week:
1. Install Google Analytics
2. Set up Google Search Console
3. Review and customize auto-generated meta descriptions
4. Add focus keywords to blog posts
5. Optimize product images

### This Month:
1. Create quality blog content (2-3 posts/week)
2. Build internal linking structure
3. Get backlinks from relevant sites
4. Monitor search performance
5. Fix any crawl errors

## 🛠️ Useful Commands

```bash
# Check SEO health
python manage.py check_seo_health

# Regenerate all SEO metadata
python manage.py generate_seo_metadata

# Optimize images for performance
python manage.py optimize_images

# Generate sitemap index
python manage.py generate_sitemap_index
```

## 📱 Admin Panel

Access SEO settings at: `/panel/`

### SEO Metadata Section:
- View/edit meta tags for all content
- Set custom titles and descriptions
- Configure Open Graph images
- Add schema markup

### Redirect Rules Section:
- Create 301/302 redirects
- Manage old URLs
- Prevent 404 errors

## 🎓 SEO Best Practices

### For Products:
- ✅ Unique titles (50-60 chars)
- ✅ Compelling descriptions (150-160 chars)
- ✅ High-quality images with alt text
- ✅ Include price and availability
- ✅ Add customer reviews

### For Blog Posts:
- ✅ Focus keyword in title
- ✅ Use H1, H2, H3 structure
- ✅ 600+ words minimum
- ✅ Internal links to products
- ✅ Engaging meta description
- ✅ Images with alt text

### For Categories:
- ✅ Unique descriptions
- ✅ Relevant keywords
- ✅ Clear hierarchy
- ✅ Breadcrumb navigation

## 📈 Monitoring

### Weekly:
- Check Google Search Console for errors
- Review new indexed pages
- Monitor click-through rates

### Monthly:
- Analyze organic traffic trends
- Review keyword rankings
- Update underperforming content
- Check page load speeds

## 🔗 Important URLs

- Sitemap: `/sitemap.xml`
- Robots: `/robots.txt`
- Admin: `/panel/`
- Google Search Console: https://search.google.com/search-console
- Google PageSpeed: https://pagespeed.web.dev/
- Rich Results Test: https://search.google.com/test/rich-results

## 🆘 Troubleshooting

### Sitemap not showing?
```bash
python manage.py migrate
# Visit: /sitemap.xml
```

### SEO metadata not appearing?
```bash
python manage.py generate_seo_metadata
# Clear browser cache
```

### Images too large?
```bash
python manage.py optimize_images --max-width=1200 --quality=85
```

## 📚 Learn More

- Full documentation: `SEO_GUIDE.md`
- Django SEO: https://docs.djangoproject.com/en/stable/ref/contrib/sitemaps/
- Google SEO Guide: https://developers.google.com/search/docs
- Schema.org: https://schema.org/

## 🎉 Success Metrics

Track these KPIs:
- Organic traffic growth
- Keyword rankings
- Click-through rate (CTR)
- Bounce rate
- Page load time
- Indexed pages count

## 💡 Pro Tips

1. **Content is King**: Publish quality content regularly
2. **Mobile First**: Ensure mobile responsiveness
3. **Speed Matters**: Optimize images and use CDN
4. **User Experience**: Easy navigation, clear CTAs
5. **Build Links**: Get quality backlinks
6. **Local SEO**: Add location info if relevant
7. **Social Signals**: Share content on social media
8. **Monitor & Adapt**: Use data to improve

---

Need help? Check `SEO_GUIDE.md` for detailed instructions.
