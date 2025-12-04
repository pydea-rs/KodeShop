from django.contrib import admin
from .models import SEOMetadata, RedirectRule


@admin.register(SEOMetadata)
class SEOMetadataAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'meta_title', 'noindex', 'updated_at')
    list_filter = ('noindex', 'nofollow', 'content_type')
    search_fields = ('meta_title', 'meta_description', 'meta_keywords')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('content_type', 'object_id', 'meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Open Graph (Facebook)', {
            'fields': ('og_title', 'og_description', 'og_image'),
            'classes': ('collapse',)
        }),
        ('Twitter Cards', {
            'fields': ('twitter_title', 'twitter_description'),
            'classes': ('collapse',)
        }),
        ('تنظیمات پیشرفته', {
            'fields': ('canonical_url', 'noindex', 'nofollow', 'schema_markup'),
            'classes': ('collapse',)
        }),
        ('اطلاعات سیستم', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(RedirectRule)
class RedirectRuleAdmin(admin.ModelAdmin):
    list_display = ('old_path', 'new_path', 'redirect_type', 'is_active', 'created_at')
    list_filter = ('redirect_type', 'is_active')
    search_fields = ('old_path', 'new_path')
