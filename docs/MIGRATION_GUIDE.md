# Database Migration Guide for SEO Updates

## Overview
This guide helps you migrate your existing database to include the new SEO fields.

## What's Being Added

### New App: `seo`
- SEOMetadata model
- RedirectRule model

### Updated Models

#### store/models.py - Product
- `meta_title` (CharField, 60 chars, optional)
- `meta_description` (CharField, 160 chars, optional)

#### post/models.py - BlogPost
- `slug` (SlugField, unique, auto-generated)
- `meta_title` (CharField, 60 chars, optional)
- `meta_description` (CharField, 160 chars, optional)
- `focus_keyword` (CharField, 100 chars, optional)

#### category/models.py - Category
- `meta_title` (CharField, 60 chars, optional)
- `meta_description` (CharField, 160 chars, optional)

## Migration Steps

### Step 1: Backup Your Database
```bash
# For SQLite
cp db.sqlite3 db.sqlite3.backup

# For PostgreSQL
pg_dump your_database > backup.sql

# For MySQL
mysqldump -u username -p database_name > backup.sql
```

### Step 2: Create Migrations
```bash
# Create migrations for updated models
python manage.py makemigrations category
python manage.py makemigrations store
python manage.py makemigrations post

# Create migrations for new SEO app
python manage.py makemigrations seo
```

### Step 3: Review Migrations
```bash
# Check what will be migrated
python manage.py showmigrations

# View SQL that will be executed (optional)
python manage.py sqlmigrate seo 0001
python manage.py sqlmigrate store 000X  # Replace X with migration number
```

### Step 4: Run Migrations
```bash
# Apply all migrations
python manage.py migrate

# Or apply specific apps
python manage.py migrate category
python manage.py migrate store
python manage.py migrate post
python manage.py migrate seo
```

### Step 5: Generate SEO Data
```bash
# Auto-generate SEO metadata for existing content
python manage.py generate_seo_metadata
```

### Step 6: Verify
```bash
# Check SEO health
python manage.py check_seo_health

# Check for any issues
python manage.py check
```

## Troubleshooting

### Issue: Migration conflicts
```bash
# If you have migration conflicts
python manage.py migrate --fake-initial

# Or merge migrations
python manage.py makemigrations --merge
```

### Issue: Slug field conflicts (BlogPost)
If you get errors about existing BlogPost records without slugs:

**Option 1: Auto-generate slugs**
```python
# Run in Django shell
python manage.py shell

from post.models import BlogPost
from django.utils.text import slugify

for blog in BlogPost.objects.filter(slug=''):
    base_slug = slugify(blog.title, allow_unicode=True)
    slug = base_slug
    counter = 1
    while BlogPost.objects.filter(slug=slug).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1
    blog.slug = slug
    blog.save()
    print(f"Generated slug for: {blog.title} -> {slug}")
```

**Option 2: Make slug nullable temporarily**
If you prefer to add slugs manually later, modify the migration:
```python
# In the migration file
migrations.AddField(
    model_name='blogpost',
    name='slug',
    field=models.SlugField(max_length=256, blank=True, null=True),
)
```

### Issue: Database locked (SQLite)
```bash
# Close all connections to the database
# Stop the development server
# Then run migrations again
python manage.py migrate
```

### Issue: Permission denied
```bash
# Ensure you have write permissions
chmod 644 db.sqlite3
# Or for the directory
chmod 755 .
```

## Rollback Instructions

If you need to rollback migrations:

### Rollback SEO app
```bash
# Rollback to before SEO was added
python manage.py migrate seo zero
```

### Rollback specific app
```bash
# Rollback to specific migration
python manage.py migrate store 0001  # Replace with previous migration number
```

### Complete rollback
```bash
# Restore from backup
cp db.sqlite3.backup db.sqlite3

# Or for PostgreSQL
psql your_database < backup.sql
```

## Post-Migration Checklist

- [ ] All migrations applied successfully
- [ ] No migration errors in console
- [ ] SEO app appears in admin panel
- [ ] Can create/edit SEO metadata
- [ ] Products have optional SEO fields
- [ ] Blog posts have slugs
- [ ] Categories have SEO fields
- [ ] `python manage.py check` shows no errors
- [ ] `python manage.py check_seo_health` runs successfully
- [ ] Website loads without errors
- [ ] Admin panel accessible
- [ ] Can view products/blogs/categories

## Testing After Migration

### 1. Test Admin Panel
```bash
# Start server
python manage.py runserver

# Visit http://localhost:8000/panel/
# Check:
# - SEO section exists
# - Can view SEO metadata
# - Can create redirect rules
```

### 2. Test Frontend
```bash
# Visit various pages:
# - Homepage: http://localhost:8000/
# - Product page: http://localhost:8000/store/category/product/
# - Blog post: http://localhost:8000/posts/blogs/1/
# - Category: http://localhost:8000/store/category/

# Check:
# - Pages load correctly
# - No 500 errors
# - Meta tags in page source
```

### 3. Test SEO Features
```bash
# Check sitemap
curl http://localhost:8000/sitemap.xml

# Check robots.txt
curl http://localhost:8000/robots.txt

# View page source and verify:
# - Meta tags present
# - Schema.org JSON-LD present
# - Open Graph tags present
```

## Common Migration Scenarios

### Scenario 1: Fresh Installation
If this is a new project with no data:
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Scenario 2: Existing Data
If you have existing products, blogs, categories:
```bash
python manage.py migrate
python manage.py generate_seo_metadata
python manage.py check_seo_health
```

### Scenario 3: Production Deployment
```bash
# 1. Backup database
# 2. Test migrations on staging first
# 3. Put site in maintenance mode
# 4. Run migrations
python manage.py migrate --no-input
python manage.py generate_seo_metadata
python manage.py collectstatic --no-input
# 5. Restart application server
# 6. Verify site works
# 7. Remove maintenance mode
```

## Database-Specific Notes

### SQLite (Development)
- Migrations are straightforward
- Backup is just copying the file
- No special considerations

### PostgreSQL (Production)
```bash
# Before migration
pg_dump dbname > backup.sql

# After migration
python manage.py migrate

# If issues, restore
psql dbname < backup.sql
```

### MySQL (Production)
```bash
# Before migration
mysqldump -u user -p dbname > backup.sql

# After migration
python manage.py migrate

# If issues, restore
mysql -u user -p dbname < backup.sql
```

## Performance Considerations

### Large Databases
If you have thousands of products/posts:

```bash
# Generate SEO metadata in batches
# Edit the management command to process in chunks
# Or run multiple times with filters

# Example: Process 100 at a time
python manage.py shell
from store.models import Product
from seo.management.commands.generate_seo_metadata import Command
cmd = Command()
# Process in batches...
```

### Indexing
After migration, consider adding indexes:
```python
# In models.py
class Meta:
    indexes = [
        models.Index(fields=['slug']),
        models.Index(fields=['created_at']),
    ]
```

## Verification Commands

```bash
# Check database integrity
python manage.py check --database default

# Check for missing migrations
python manage.py showmigrations

# Check for model issues
python manage.py check

# Validate templates
python manage.py validate_templates

# Check SEO health
python manage.py check_seo_health
```

## Support

If you encounter issues:

1. Check error messages carefully
2. Review migration files
3. Check database logs
4. Verify model definitions
5. Test on a copy of the database first
6. Consult Django documentation: https://docs.djangoproject.com/en/stable/topics/migrations/

## Summary

The migration process adds:
- 1 new app (seo)
- 2 new models (SEOMetadata, RedirectRule)
- 7 new fields across existing models
- Multiple management commands
- Template tags and utilities

All fields are optional (blank=True), so existing data won't break.

After successful migration, run:
```bash
python manage.py generate_seo_metadata
python manage.py check_seo_health
```

Your site will then be fully SEO-optimized! 🚀
