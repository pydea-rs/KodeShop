from django.shortcuts import redirect
from django.urls import resolve
from .models import RedirectRule


class SEORedirectMiddleware:
    """
    Middleware to handle 301/302 redirects for SEO
    """
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        path = request.path
        
        try:
            redirect_rule = RedirectRule.objects.get(old_path=path, is_active=True)
            return redirect(redirect_rule.new_path, permanent=(redirect_rule.redirect_type == 301))
        except RedirectRule.DoesNotExist:
            pass
        
        response = self.get_response(request)
        return response


class SecurityHeadersMiddleware:
    """
    Add security headers for better SEO and security
    """
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        
        # Security headers
        response['X-Content-Type-Options'] = 'nosniff'
        response['X-Frame-Options'] = 'SAMEORIGIN'
        response['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        
        return response
