import json

from django.shortcuts import render, get_object_or_404, redirect
from category.models import Category
from .models import Product, Review, Gallery
from .forms import ReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from kodeshop.utils import PaginationParams

def store(request, category_filter=None):
    from django.contrib.contenttypes.models import ContentType
    from seo.models import SEOMetadata
    
    max_price = min_price = 0
    current_category = None
    filters = Q()
    try:
        if category_filter:
            obj_expected_categories = get_object_or_404(Category, slug=category_filter)
            current_category = obj_expected_categories
            if obj_expected_categories:
                filters &= Q(category=obj_expected_categories)

        if request.method == "POST":
            try:
                min_price = int(request.POST["min_price"])
            except:
                min_price = 0

            try:
                max_price = int(request.POST["max_price"])
            except:
                max_price = 0

            if min_price > 0:
                filters &= Q(price__gte=min_price)
            if max_price > 0:
                filters &= Q(price__lte=max_price)
    except Exception as ex:
        print(ex.__str__())

    pagination = PaginationParams(request, Product, filters)
    products = pagination.get_items('created', order_descending=True)
    
    # SEO metadata
    meta_title = 'فروشگاه - خرید آنلاین ابزار کشاورزی'
    meta_description = 'خرید آنلاین ابزار و تجهیزات کشاورزی با بهترین قیمت و کیفیت'
    breadcrumbs = [{'name': 'خانه', 'url': '/'}, {'name': 'فروشگاه', 'url': '/store/'}]
    
    if current_category:
        meta_title = f"{current_category.name_fa} - خرید آنلاین"
        meta_description = current_category.description if current_category.description else f"خرید {current_category.name_fa} با بهترین قیمت"
        breadcrumbs.append({'name': current_category.name_fa, 'url': current_category.url()})
        
        # Get SEO metadata for category
        content_type = ContentType.objects.get_for_model(current_category)
        try:
            seo_data = SEOMetadata.objects.get(content_type=content_type, object_id=current_category.id)
            if seo_data.meta_title:
                meta_title = seo_data.meta_title
            if seo_data.meta_description:
                meta_description = seo_data.meta_description
        except SEOMetadata.DoesNotExist:
            pass
    
    context = {
        'products': products,
        'products_count': products.count() if products else 0,
        'current_category': current_category,
        'category_filter': category_filter,
        'max_price': max_price,
        'min_price': min_price,
        'pagination': pagination,
        'meta_title': meta_title,
        'meta_description': meta_description,
        'breadcrumbs': breadcrumbs,
    }

    return render(request, 'store/store.html', context)


def product(request, category_filter, product_slug=None):
    from seo.utils import generate_product_schema
    from django.contrib.contenttypes.models import ContentType
    from seo.models import SEOMetadata
    
    context = dict()
    try:
        this_product = Product.objects.get(slug=product_slug, category__slug=category_filter)
        reviews = Review.objects.filter(product=this_product, status=True)
        gallery = Gallery.objects.filter(product=this_product)
        
        # Get or create SEO metadata
        content_type = ContentType.objects.get_for_model(this_product)
        try:
            seo_data = SEOMetadata.objects.get(content_type=content_type, object_id=this_product.id)
        except SEOMetadata.DoesNotExist:
            seo_data = None
        
        # Generate schema markup
        schema_markup = generate_product_schema(this_product)
        
        # Build breadcrumbs
        breadcrumbs = [
            {'name': 'خانه', 'url': '/'},
            {'name': 'فروشگاه', 'url': '/store/'},
            {'name': this_product.category.name_fa, 'url': this_product.category.url()},
            {'name': this_product.name_fa, 'url': this_product.url()},
        ]
        
        context = {
            'this_product': this_product,
            'reviews': reviews,
            'gallery': gallery,
            'meta_title': f"{this_product.name_fa} - خرید آنلاین",
            'meta_description': this_product.description[:160] if this_product.description else f"خرید {this_product.name_fa} با بهترین قیمت و کیفیت",
            'meta_keywords': f"{this_product.name_fa}, {this_product.category.name_fa}, خرید آنلاین",
            'og_type': 'product',
            'og_image': request.build_absolute_uri(this_product.image.url) if this_product.image else None,
            'schema_markup': schema_markup,
            'breadcrumbs': breadcrumbs,
            'seo_data': seo_data,
        }
        
        # Set for context processor
        request.seo_object = this_product
        
    except Exception as ex:
        # handle this seriously
        raise ex

    return render(request, 'store/product.html', context)


@login_required(login_url='login')
def post_review(request, product_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                old_review = Review.objects.get(user__id=request.user.id, product__id=product_id)
                form = ReviewForm(request.POST, instance=old_review)  # instance=review parameter will prevent from
                # django from creating new review, and it will replace existing one
                form.save()
                messages.info(request, "نظر شما به روز رسانی شد.")
            except Review.DoesNotExist:
                form = ReviewForm(request.POST)
                if form.is_valid():
                    try:
                        product_to_be_reviewed = Product.objects.get(id=product_id)
                        new_review = Review(product=product_to_be_reviewed, user=request.user,
                                            comment=form.cleaned_data['comment'], rating=form.cleaned_data['rating'],
                                            ip=request.META.get('REMOTE_ADDR'))
                        # validate form and ip first
                        new_review.save()
                        messages.success(request, 'نظر شما ثبت شد.')
                    except Product.DoesNotExist:
                        messages.error(request, 'متاسفانه چنین کالایی وجود ندارد. در نتیجه نظر شما را نمی توانیم ثبت '
                                                'کنیم.')
    else:
        messages.error(request, 'برای ارسال نظر ابتدا باید وارد حساب کاربری خود شوید.')
    return redirect(request.META.get('HTTP_REFERER'))