#!/bin/bash

echo "=========================================="
echo "KodeShop SEO Setup Script"
echo "=========================================="
echo ""

# Check if virtual environment is activated
if [ -z "$VIRTUAL_ENV" ]; then
    echo "⚠️  Warning: No virtual environment detected"
    echo "It's recommended to activate your virtual environment first"
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

echo "Step 1: Creating SEO migrations..."
python manage.py makemigrations seo
if [ $? -ne 0 ]; then
    echo "❌ Failed to create migrations"
    exit 1
fi

echo ""
echo "Step 2: Running migrations..."
python manage.py migrate
if [ $? -ne 0 ]; then
    echo "❌ Failed to run migrations"
    exit 1
fi

echo ""
echo "Step 3: Generating SEO metadata for existing content..."
python manage.py generate_seo_metadata
if [ $? -ne 0 ]; then
    echo "⚠️  Warning: Failed to generate SEO metadata"
    echo "You can run this manually later: python manage.py generate_seo_metadata"
fi

echo ""
echo "Step 4: Checking SEO health..."
python manage.py check_seo_health

echo ""
echo "=========================================="
echo "✅ SEO Setup Complete!"
echo "=========================================="
echo ""
echo "Next Steps:"
echo "1. Review SEO metadata in admin panel: /panel/"
echo "2. Update .env file with SEO variables (see .env.example)"
echo "3. Submit sitemap to Google Search Console: /sitemap.xml"
echo "4. Configure robots.txt if needed"
echo "5. Read SEO_GUIDE.md for detailed instructions"
echo ""
echo "Useful Commands:"
echo "  - Check SEO health: python manage.py check_seo_health"
echo "  - Regenerate metadata: python manage.py generate_seo_metadata"
echo "  - Optimize images: python manage.py optimize_images"
echo ""
