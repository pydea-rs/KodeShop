"""
SEO Analyzer - Analyze content for SEO best practices
"""
import re
from bs4 import BeautifulSoup


class SEOAnalyzer:
    """
    Analyze content for SEO optimization
    """
    
    def __init__(self, content, title='', description='', focus_keyword=''):
        self.content = content
        self.title = title
        self.description = description
        self.focus_keyword = focus_keyword.lower()
        self.soup = BeautifulSoup(content, 'html.parser') if content else None
        self.issues = []
        self.score = 100
    
    def analyze(self):
        """
        Run all SEO checks
        """
        self.check_title()
        self.check_description()
        self.check_keyword_density()
        self.check_headings()
        self.check_images()
        self.check_links()
        self.check_content_length()
        
        return {
            'score': max(0, self.score),
            'issues': self.issues,
            'grade': self.get_grade()
        }
    
    def check_title(self):
        """Check title optimization"""
        if not self.title:
            self.add_issue('No title provided', 10)
            return
        
        title_length = len(self.title)
        if title_length < 30:
            self.add_issue('Title is too short (< 30 characters)', 5)
        elif title_length > 60:
            self.add_issue('Title is too long (> 60 characters)', 5)
        
        if self.focus_keyword and self.focus_keyword not in self.title.lower():
            self.add_issue('Focus keyword not in title', 8)
    
    def check_description(self):
        """Check meta description"""
        if not self.description:
            self.add_issue('No meta description provided', 10)
            return
        
        desc_length = len(self.description)
        if desc_length < 120:
            self.add_issue('Meta description is too short (< 120 characters)', 5)
        elif desc_length > 160:
            self.add_issue('Meta description is too long (> 160 characters)', 5)
        
        if self.focus_keyword and self.focus_keyword not in self.description.lower():
            self.add_issue('Focus keyword not in meta description', 5)
    
    def check_keyword_density(self):
        """Check keyword density"""
        if not self.focus_keyword or not self.content:
            return
        
        text = self.soup.get_text().lower() if self.soup else self.content.lower()
        words = text.split()
        total_words = len(words)
        
        if total_words == 0:
            return
        
        keyword_count = text.count(self.focus_keyword)
        density = (keyword_count / total_words) * 100
        
        if density < 0.5:
            self.add_issue('Keyword density too low (< 0.5%)', 5)
        elif density > 3:
            self.add_issue('Keyword density too high (> 3%) - may be keyword stuffing', 8)
    
    def check_headings(self):
        """Check heading structure"""
        if not self.soup:
            return
        
        h1_tags = self.soup.find_all('h1')
        if len(h1_tags) == 0:
            self.add_issue('No H1 heading found', 10)
        elif len(h1_tags) > 1:
            self.add_issue('Multiple H1 headings found', 5)
        
        if self.focus_keyword:
            h1_text = ' '.join([h.get_text().lower() for h in h1_tags])
            if self.focus_keyword not in h1_text:
                self.add_issue('Focus keyword not in H1 heading', 5)
    
    def check_images(self):
        """Check image optimization"""
        if not self.soup:
            return
        
        images = self.soup.find_all('img')
        images_without_alt = [img for img in images if not img.get('alt')]
        
        if images_without_alt:
            self.add_issue(f'{len(images_without_alt)} images missing alt text', 5)
    
    def check_links(self):
        """Check internal and external links"""
        if not self.soup:
            return
        
        links = self.soup.find_all('a')
        internal_links = [link for link in links if link.get('href', '').startswith('/')]
        external_links = [link for link in links if link.get('href', '').startswith('http')]
        
        if len(internal_links) == 0:
            self.add_issue('No internal links found', 3)
        
        if len(external_links) > 0:
            external_without_nofollow = [
                link for link in external_links 
                if 'nofollow' not in link.get('rel', [])
            ]
            if len(external_without_nofollow) > 5:
                self.add_issue('Consider adding nofollow to some external links', 2)
    
    def check_content_length(self):
        """Check content length"""
        if not self.content:
            self.add_issue('No content provided', 15)
            return
        
        text = self.soup.get_text() if self.soup else self.content
        word_count = len(text.split())
        
        if word_count < 300:
            self.add_issue('Content is too short (< 300 words)', 10)
        elif word_count < 600:
            self.add_issue('Content could be longer for better SEO (< 600 words)', 3)
    
    def add_issue(self, message, penalty):
        """Add an issue and reduce score"""
        self.issues.append(message)
        self.score -= penalty
    
    def get_grade(self):
        """Get letter grade based on score"""
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        elif self.score >= 70:
            return 'C'
        elif self.score >= 60:
            return 'D'
        else:
            return 'F'


def analyze_product_seo(product):
    """
    Analyze a product for SEO
    """
    analyzer = SEOAnalyzer(
        content=product.description,
        title=product.name_fa,
        description=product.description[:160] if product.description else '',
        focus_keyword=product.name_fa
    )
    return analyzer.analyze()


def analyze_blog_seo(blog_post):
    """
    Analyze a blog post for SEO
    """
    analyzer = SEOAnalyzer(
        content=blog_post.body,
        title=blog_post.title,
        description=blog_post.summary if blog_post.summary else '',
        focus_keyword=blog_post.focus_keyword if hasattr(blog_post, 'focus_keyword') else ''
    )
    return analyzer.analyze()
