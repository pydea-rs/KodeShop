from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class SEOMetadata(models.Model):
    """
    Generic SEO metadata model that can be attached to any model
    """
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    meta_title = models.CharField(max_length=60, blank=True, verbose_name='عنوان متا (SEO)')
    meta_description = models.CharField(max_length=160, blank=True, verbose_name='توضیحات متا (SEO)')
    meta_keywords = models.CharField(max_length=255, blank=True, verbose_name='کلمات کلیدی')
    
    og_title = models.CharField(max_length=95, blank=True, verbose_name='عنوان Open Graph')
    og_description = models.CharField(max_length=200, blank=True, verbose_name='توضیحات Open Graph')
    og_image = models.ImageField(upload_to='seo/og_images/', blank=True, null=True, verbose_name='تصویر Open Graph')
    
    twitter_title = models.CharField(max_length=70, blank=True, verbose_name='عنوان Twitter')
    twitter_description = models.CharField(max_length=200, blank=True, verbose_name='توضیحات Twitter')
    
    canonical_url = models.URLField(blank=True, verbose_name='URL کانونیکال')
    noindex = models.BooleanField(default=False, verbose_name='عدم نمایه سازی')
    nofollow = models.BooleanField(default=False, verbose_name='عدم دنبال کردن لینک‌ها')
    
    schema_markup = models.JSONField(blank=True, null=True, verbose_name='Schema.org JSON-LD')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'متادیتای SEO'
        verbose_name_plural = 'متادیتاهای SEO'
        unique_together = ('content_type', 'object_id')
    
    def __str__(self):
        return f"SEO for {self.content_object}"


class RedirectRule(models.Model):
    """
    301/302 redirects for SEO
    """
    REDIRECT_TYPES = (
        (301, '301 - دائمی'),
        (302, '302 - موقت'),
    )
    
    old_path = models.CharField(max_length=255, unique=True, verbose_name='مسیر قدیمی')
    new_path = models.CharField(max_length=255, verbose_name='مسیر جدید')
    redirect_type = models.IntegerField(choices=REDIRECT_TYPES, default=301, verbose_name='نوع ریدایرکت')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'قانون ریدایرکت'
        verbose_name_plural = 'قوانین ریدایرکت'
    
    def __str__(self):
        return f"{self.old_path} -> {self.new_path} ({self.redirect_type})"
